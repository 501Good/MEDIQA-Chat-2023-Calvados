---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: long-t5-tglobal-base-taskAB-pegasus2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# long-t5-tglobal-base-taskAB-pegasus2

This model is a fine-tuned version of [google/long-t5-tglobal-base](https://huggingface.co/google/long-t5-tglobal-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1990
- Rouge1: 45.4946
- Rouge2: 28.4027
- Rougel: 41.0221
- Rougelsum: 43.7338
- Gen Len: 117.2994

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 0
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.04
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len  |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:--------:|
| 6.1614        | 1.0   | 181  | 2.6093          | 19.1631 | 8.7842  | 17.2095 | 18.1737   | 231.8192 |
| 2.7913        | 2.0   | 362  | 1.8072          | 28.0003 | 15.7042 | 26.4042 | 27.1145   | 138.8475 |
| 2.2025        | 3.0   | 543  | 1.5130          | 30.9777 | 19.114  | 29.1024 | 29.6909   | 120.0508 |
| 1.7267        | 4.0   | 724  | 1.3892          | 31.6675 | 19.7428 | 29.8595 | 30.6269   | 155.4972 |
| 1.6593        | 5.0   | 905  | 1.3246          | 34.5528 | 21.2936 | 32.1899 | 33.2958   | 107.5819 |
| 1.4994        | 6.0   | 1086 | 1.2841          | 36.1465 | 23.0778 | 33.2726 | 34.7078   | 111.2203 |
| 1.5312        | 7.0   | 1267 | 1.2571          | 37.8915 | 24.1156 | 35.2534 | 36.6519   | 86.3051  |
| 1.3896        | 8.0   | 1448 | 1.2326          | 39.0301 | 24.4935 | 35.7931 | 37.3982   | 100.3164 |
| 1.3874        | 9.0   | 1629 | 1.2176          | 39.8924 | 25.7213 | 36.754  | 38.5612   | 92.5198  |
| 1.2213        | 10.0  | 1810 | 1.2153          | 39.6051 | 25.563  | 36.5707 | 38.0116   | 105.8531 |
| 1.1912        | 11.0  | 1991 | 1.2078          | 38.4868 | 24.5791 | 35.5639 | 37.0012   | 116.5424 |
| 1.2209        | 12.0  | 2172 | 1.1991          | 38.6529 | 24.7519 | 35.4157 | 37.0278   | 117.5198 |
| 1.1436        | 13.0  | 2353 | 1.2032          | 41.1449 | 26.3206 | 37.8393 | 39.4769   | 101.4520 |
| 1.1755        | 14.0  | 2534 | 1.1888          | 41.4317 | 26.4915 | 37.9296 | 39.6725   | 117.8475 |
| 1.1311        | 15.0  | 2715 | 1.1971          | 43.3421 | 27.4992 | 39.1124 | 41.4943   | 119.2938 |
| 1.0614        | 16.0  | 2896 | 1.1888          | 43.8944 | 27.9972 | 39.9138 | 41.976    | 112.8701 |
| 1.0506        | 17.0  | 3077 | 1.2006          | 44.5282 | 28.1328 | 39.9487 | 42.6861   | 115.7119 |
| 1.0601        | 18.0  | 3258 | 1.1945          | 44.2954 | 27.8845 | 39.606  | 42.497    | 117.5593 |
| 1.0895        | 19.0  | 3439 | 1.1943          | 44.6755 | 28.3186 | 40.2528 | 42.9491   | 113.4407 |
| 1.0367        | 20.0  | 3620 | 1.1917          | 44.9575 | 28.3342 | 40.5697 | 43.0845   | 138.1695 |
| 1.0267        | 21.0  | 3801 | 1.1929          | 45.4458 | 28.6146 | 40.6464 | 43.7194   | 128.0508 |
| 1.0126        | 22.0  | 3982 | 1.1913          | 45.707  | 28.8296 | 40.9974 | 43.9395   | 131.6045 |
| 0.9696        | 23.0  | 4163 | 1.1943          | 44.584  | 27.8436 | 39.9967 | 42.8648   | 126.2994 |
| 0.937         | 24.0  | 4344 | 1.1898          | 45.6413 | 28.4939 | 41.1178 | 43.9735   | 117.5254 |
| 0.9735        | 25.0  | 4525 | 1.1990          | 45.8929 | 28.6341 | 41.4747 | 44.1398   | 117.4802 |
| 0.9458        | 26.0  | 4706 | 1.2008          | 45.7909 | 28.9536 | 41.4398 | 44.0397   | 121.4972 |
| 0.9477        | 27.0  | 4887 | 1.1962          | 45.2462 | 28.0785 | 40.6127 | 43.3662   | 128.2203 |
| 0.9759        | 28.0  | 5068 | 1.1991          | 45.0664 | 28.0082 | 40.5041 | 43.2468   | 120.2712 |
| 0.9166        | 29.0  | 5249 | 1.1993          | 45.4258 | 28.3867 | 40.9383 | 43.6698   | 117.5763 |
| 0.9493        | 30.0  | 5430 | 1.1990          | 45.4946 | 28.4027 | 41.0221 | 43.7338   | 117.2994 |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.0+cu116
- Datasets 2.10.1
- Tokenizers 0.13.2
