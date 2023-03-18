#!/bin/bash

python3 run_inference_taskA_run1.py --input_file_name $1 --output_file_name taskA_Calvados_run2.csv \
    --model_name saved_models/long-t5-tglobal-base-taskAB-pegasus2 --tagging_strategy same --prefix "summarize short: " \
    --num_beams 1 --top_k 5 --penalty_alpha 0.6 --no_early_stopping
