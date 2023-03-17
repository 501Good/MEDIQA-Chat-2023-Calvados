from datasets import load_dataset
import sys
import pandas as pd

from code.stanza_utils import insert_taskB_tag
from code.utils import dialogue_to_chunks

summarizer = pipeline("summarization", model="long-t5-tglobal-base-taskB-4")
divisions = {'assessment_and_plan', 'objective_exam', 'objective_results', 'subjective'}

sys_args = sys.argv
print(sys_args[1])
file_name = sys_args[1].split('.')[-2]
dataset = load_dataset('csv', data_files={'inference': sys_args[1]})

tagged_df = [insert_taskB_tag(t) for t in dataset['inference']]
# tagged_df = pd.DataFrame.from_dict(tagged_df)
# tagged_df.to_csv(f"./{file_name}(tagged).csv")

final_output = []

final_text = ""
for d in tagged_df:
	current_data = {}
	for division in divisions:
	    res = summarizer(f"Generate {division} note:\n" + d['dialogue'] + '\nNote:\n', min_length=10, max_length=512, penalty_alpha=0.6, top_k=4, num_beams=1)
	    if division == "subjective":
	    	final_text = final_text + f"\n\nHISTORY OF PRESENT ILLNESS\n{res[0]['summary_text']}"
	    if division == "objective_exam":
	    	final_text = final_text + f"\n\nPHYSICAL EXAM\n{res[0]['summary_text']}"
	    if division == "objective_results":
	    	final_text = final_text + f"\n\nRESULTS\n{res[0]['summary_text']}"
	    if "assesment" in division:
	    	final_text = final_text + f"\n\nASSESSMENT AND PLAN\n{res[0]['summary_text']}"
	    # print(f"long-t5-tglobal-base-taskB summary for {division}:\n{res[0]['summary_text']}\n---------------")
    current_data['TestID'] = d['ID']
    current_data['SystemOutput'] = final_text
    final_output.append(current_data)

final_output = pd.DataFrame.from_dict(final_output)
final_output.to_csv("./outputs/taskB_Calvados_run1.csv", index=False)