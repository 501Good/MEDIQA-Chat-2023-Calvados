import stanza

nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'}, use_gpu=True)

def insert_taskA_tag(sample):
    dialogue = sample["dialogue"]
    dialogue_tags = nlp(sample["dialogue"])
    for t in dialogue_tags.entities:
        t = t.to_dict()
        dialogue = dialogue.replace(t['text'], f"<extra_id_0> {t['text']} <extra_id_0>")
    while "<extra_id_0> <extra_id_0>" in dialogue:
        dialogue = dialogue.replace("<extra_id_0> <extra_id_0>", "<extra_id_0>")
    sample['dialogue'] = dialogue
    
    '''
    section_text = sample['section_text']
    section_tags = nlp(section_text)
    for t in section_tags.entities:
        t = t.to_dict()
        section_text = section_text.replace(t['text'], f"<extra_id_0> {t['text']} <extra_id_0>")
    while "<extra_id_0> <extra_id_0>" in section_text:
        section_text = section_text.replace("<extra_id_0> <extra_id_0>", "<extra_id_0>")
    sample['section_text'] = section_text
    '''
    return sample


def insert_taskB_tag(sample):
    dialogue = sample["dialogue"]
    dialogue_tags = nlp(sample["dialogue"])
    for t in dialogue_tags.entities:
        t = t.to_dict()
        dialogue = dialogue.replace(t['text'], f"<extra_id_0> {t['text']} <extra_id_0>")
    while "<extra_id_0> <extra_id_0>" in dialogue:
        dialogue = dialogue.replace("<extra_id_0> <extra_id_0>", "<extra_id_0>")
    sample['dialogue'] = dialogue
    
    section_text = sample['note']
    section_tags = nlp(section_text)
    for t in section_tags.entities:
        t = t.to_dict()
        section_text = section_text.replace(t['text'], f"<extra_id_0> {t['text']} <extra_id_0>")
    while "<extra_id_0> <extra_id_0>" in section_text:
        section_text = section_text.replace("<extra_id_0> <extra_id_0>", "<extra_id_0>")
    sample['note'] = section_text
    return sample
