import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import re

import pandas as pd
import torch
from datasets import load_dataset
from tqdm import tqdm
from transformers import HfArgumentParser, pipeline
from nltk.tokenize.treebank import TreebankWordDetokenizer

from src.stanza_utils import insert_taskB_tag


@dataclass
class GenerationArguments:
    input_file_name: Optional[str] = field(
        default=None, metadata={"help": "Path to the CSV file with the inputs."}
    )
    output_file_name: Optional[str] = field(
        default=None, metadata={"help": "Path to the CSV file with the system outputs."}
    )
    model_name: Optional[str] = field(
        default=None, metadata={"help": "Name of the model to use."}
    )
    prefix: Optional[str] = field(
        default='', metadata={"help": "Task-specific prefix for the T5 model."}
    )
    tagging_strategy: Optional[str] = field(default='different', metadata={"help": (
        "The type of markings to use. different will put different tags for the beginning and the end of sequence and "
        "same will put the same tag.")})

    def __post_init__(self):
        if self.input_file_name is None:
            raise ValueError("input_file_name must be set!")
        if self.output_file_name is None:
            raise ValueError("output_file_name must be set!")
        if self.model_name is None:
            raise ValueError("model_name must be set!")
        if self.tagging_strategy not in ['different', 'same']:
            raise ValueError(f"tagging_strategy must be either 'different' or 'same'! Got '{self.tagging_strategy}'.")


@dataclass
class DecodingArguments:
    num_beams: Optional[int] = field(
        default=4, metadata={"help": "Number of beams for beam search. 1 means no beam search."}
    )
    no_repeat_ngram_size: Optional[int] = field(
        default=3, metadata={"help": "If set to int > 0, all ngrams of that size can only occur once."}
    )
    early_stopping: Optional[bool] = field(default=True, metadata={"help": (
        "Controls the stopping condition for beam-based methods, like beam-search. It accepts the following values: "
        "True, where the generation stops as soon as there are num_beams complete candidates; False, where an "
        "heuristic is applied and the generation stops when is it very unlikely to find better candidates; \"never\", "
        "where the beam search procedure only stops when there cannot be better candidates "
        "(canonical beam search algorithm).")})
    length_penalty: Optional[float] = field(default=2.0, metadata={"help": (
        "Exponential penalty to the length that is used with beam-based generation. It is applied as an exponent to "
        "the sequence length, which in turn is used to divide the score of the sequence. Since the score is the log "
        "likelihood of the sequence (i.e. negative), length_penalty > 0.0 promotes longer sequences, while "
        "length_penalty < 0.0 encourages shorter sequences.")})
    max_length: Optional[int] = field(default=200, metadata={"help": (
        "The maximum length the generated tokens can have. Corresponds to the length of the input prompt + "
        "max_new_tokens. Its effect is overridden by max_new_tokens, if also set.")})
    top_k: Optional[int] = field(
        default=50,
        metadata={"help": "The number of highest probability vocabulary tokens to keep for top-k-filtering."})
    penalty_alpha: Optional[float] = field(
        default=None,
        metadata={"help": "The values balance the model confidence and the degeneration penalty in contrastive search decoding."})

    def __post_init__(self):
        pass


def main():

    parser = HfArgumentParser((GenerationArguments, DecodingArguments))
    generation_args, decoding_args = parser.parse_args_into_dataclasses()

    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
    twd = TreebankWordDetokenizer()

    model_id = generation_args.model_name
    summarizer = pipeline("summarization", model=model_id, device=device)

    divisions = ['subjective', 'objective_exam', 'objective_results', 'assessment_and_plan']

    file_name = str(Path(generation_args.input_file_name))
    dataset = load_dataset('csv', data_files={'inference': file_name})

    tagged_df = [insert_taskB_tag(t) for t in tqdm(dataset['inference'])]
    # tagged_df = pd.DataFrame.from_dict(tagged_df)
    # tagged_df.to_csv(f"./{file_name}(tagged).csv")

    final_output = []

    for d in tqdm(tagged_df):
        final_text = ""
        current_data = {}

        dialogue = d['dialogue'].replace("[doctor]", "Doctor:").replace("[patient]", "Patient:")
        dialogue = re.sub(' \. ([a-z])', r'. \1', dialogue)
        dialogue = '\n'.join([twd.detokenize(line.split()) for line in dialogue.split('\n')])

        for division in divisions:
            res = summarizer(
                f"summarize {division}: " + dialogue,
                num_beams=decoding_args.num_beams,
                no_repeat_ngram_size=decoding_args.no_repeat_ngram_size,
                early_stopping=decoding_args.early_stopping,
                length_penalty=decoding_args.length_penalty,
                max_length=decoding_args.max_length,
                top_k=decoding_args.top_k,
                penalty_alpha=decoding_args.penalty_alpha,
            )
            summary = ' '.join(res[0]['summary_text'].split(' ')[2:])
            if division == "subjective":
                if "HISTORY OF PRESENT ILLNESS" not in summary:
                    final_text = final_text + f"HISTORY OF PRESENT ILLNESS\n\n{summary}"
                else:
                    final_text = final_text + summary
            if division == "objective_exam":
                if "PHYSICAL EXAM" not in summary:
                    final_text = final_text + f"\n\nPHYSICAL EXAM\n\n{summary}"
                else:
                    final_text = final_text + '\n\n' + summary
            if division == "objective_results":
                if "RESULTS" not in summary:
                    final_text = final_text + f"\n\nRESULTS\n\n{summary}"
                else:
                    final_text = final_text + '\n\n' + summary
            if division == "assessment_and_plan":
                if "ASSESSMENT AND PLAN" in summary:
                    final_text = final_text + f"\n\nASSESSMENT AND PLAN\n\n{summary}"
                else:
                    final_text = final_text + '\n\n' + summary
        current_data['TestID'] = d['encounter_id']
        current_data['SystemOutput'] = final_text
        final_output.append(current_data)

    output_dir = Path('outputs')
    final_output = pd.DataFrame.from_dict(final_output)
    final_output.to_csv(output_dir / generation_args.output_file_name, index=False)


if __name__ == "__main__":
    main()
