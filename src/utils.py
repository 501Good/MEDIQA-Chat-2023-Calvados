from nltk.tokenize.treebank import TreebankWordDetokenizer
import re

def dialogue_to_chunks(dialogue):
	twd = TreebankWordDetokenizer()
	dialogue = re.sub(' \. ([a-z])', r'. \1', dialogue)
	lines = []
	for line in dialogue.split('\n'):
	    lines.append(twd.detokenize(line.split()))
	    
	chunks = []
	chunk = []
	doctor_counter = 0
	for line in lines:
	    if line.startswith('Doctor:'):
	        if doctor_counter == 5:
	            chunks.append('\n'.join(chunk))
	            chunk = []
	            doctor_counter = 1
	        else:
	            doctor_counter += 1
	    chunk.append(line)
	chunks.append('\n'.join(chunk))
	return chunks