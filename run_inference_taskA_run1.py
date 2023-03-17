from datasets import load_dataset
import sys
import pandas as pd
from transformers import pipeline

from src.stanza_utils import insert_taskA_tag

tokenizer_model_id = "google/flan-t5-base"
generation_model_id = "google/flan-t5-base"

model_id = "flan-t5-base-taskA-stanza-2SpecialTag-LR5e-5"
summarizer = pipeline("summarization", model=model_id)

sys_args = sys.argv
print(sys_args[1])
file_name = sys_args[1].split('.')[-2]
dataset = load_dataset('csv', data_files={'inference': sys_args[1]})

tagged_df = [insert_taskA_tag(t) for t in dataset['inference']]
# tagged_df = pd.DataFrame.from_dict(tagged_df)
# tagged_df.to_csv(f"./{file_name}(tagged).csv")

final_output = []
for i, d in enumerate(tagged_df):
    current_data = {}
    #current_data['id'] = i
    current_data['TestID'] = d['ID']
    text = summarizer(d['dialogue'])
    text = text[0]['summary_text']
    print(type(text[0]))
    section_header = text.split(" ")[2]
    section_text = " ".join(text.split(" ")[5:])
    current_data['SystemOutput1'] = section_header
    while "  " in section_text:
        section_text = section_text.replace("  ", " ")
    current_data['SystemOutput2'] = section_text
    final_output.append(current_data)

final_output = pd.DataFrame.from_dict(final_output)
final_output.to_csv("./outputs/taskA_Calvados_run1.csv", index=False)
