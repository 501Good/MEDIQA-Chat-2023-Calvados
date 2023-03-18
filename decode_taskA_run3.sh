#!/bin/bash

python3 run_inference_taskA_run1.py --input_file_name $1 --output_file_name taskA_Calvados_run3.csv \
    --model_name saved_models/flan-t5-base-taskA-stanza-2SpecialTag-LR5e-5
