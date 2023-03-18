#!/bin/bash

python3 run_inference_taskB_run1.py --input_file_name $1 --output_file_name taskB_Calvados_run1.csv \
    --model_name saved_models/long-t5-tglobal-base-taskAB-pegasus2 --tagging_strategy same --max_length 512
