---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: flan-t5-base-taskA-stanza-2SpecialTag-LR5e-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-base-taskA-stanza-2SpecialTag-LR5e-5

This model is a fine-tuned version of [google/flan-t5-base](https://huggingface.co/google/flan-t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1346
- Rouge1: 46.4472
- Rouge2: 35.46
- Rougel: 45.1554
- Rougelsum: 45.8231
- Gen Len: 18.59

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
- train_batch_size: 3
- eval_batch_size: 3
- seed: 0
- gradient_accumulation_steps: 8
- total_train_batch_size: 24
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.04
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 5.9645        | 1.0   | 50   | 3.4877          | 11.3078 | 3.3485  | 10.3046 | 10.8701   | 14.4    |
| 2.4075        | 2.0   | 100  | 1.4956          | 36.8015 | 22.5896 | 36.2476 | 36.8897   | 18.87   |
| 1.5455        | 3.0   | 150  | 1.3226          | 41.9688 | 29.4155 | 41.1456 | 41.5917   | 18.55   |
| 1.3453        | 4.0   | 200  | 1.2621          | 43.2308 | 30.3023 | 42.21   | 42.7117   | 18.48   |
| 1.2515        | 5.0   | 250  | 1.1986          | 43.9957 | 31.2399 | 42.551  | 43.2555   | 18.67   |
| 1.1859        | 6.0   | 300  | 1.1753          | 44.3545 | 31.9053 | 43.0954 | 43.6229   | 18.65   |
| 1.1299        | 7.0   | 350  | 1.1572          | 45.8976 | 33.9281 | 44.7895 | 45.2868   | 18.63   |
| 1.0854        | 8.0   | 400  | 1.1458          | 45.6928 | 33.931  | 44.6149 | 45.2287   | 18.53   |
| 1.0483        | 9.0   | 450  | 1.1326          | 46.1105 | 34.8511 | 45.0796 | 45.7382   | 18.6    |
| 1.0194        | 10.0  | 500  | 1.1193          | 46.8337 | 36.1321 | 45.7709 | 46.2772   | 18.56   |
| 0.9953        | 11.0  | 550  | 1.1194          | 47.0184 | 35.7303 | 45.9069 | 46.4367   | 18.62   |
| 0.9683        | 12.0  | 600  | 1.1247          | 46.9858 | 36.0828 | 45.8322 | 46.4075   | 18.51   |
| 0.9495        | 13.0  | 650  | 1.1170          | 46.5613 | 35.9417 | 45.4811 | 46.0043   | 18.62   |
| 0.9276        | 14.0  | 700  | 1.1177          | 46.9637 | 35.9778 | 45.7787 | 46.2627   | 18.55   |
| 0.9121        | 15.0  | 750  | 1.1184          | 46.0268 | 35.3245 | 44.8404 | 45.423    | 18.61   |
| 0.8977        | 16.0  | 800  | 1.1137          | 46.504  | 35.4906 | 45.2924 | 45.9369   | 18.52   |
| 0.881         | 17.0  | 850  | 1.1235          | 46.4522 | 35.403  | 45.2726 | 45.8208   | 18.48   |
| 0.867         | 18.0  | 900  | 1.1206          | 46.4102 | 35.3509 | 45.3162 | 45.8517   | 18.46   |
| 0.8593        | 19.0  | 950  | 1.1143          | 46.5142 | 35.4639 | 45.3639 | 46.0655   | 18.62   |
| 0.8458        | 20.0  | 1000 | 1.1273          | 46.3375 | 35.6955 | 45.2334 | 45.9046   | 18.51   |
| 0.8327        | 21.0  | 1050 | 1.1243          | 46.3788 | 36.0158 | 45.3357 | 45.9592   | 18.56   |
| 0.8285        | 22.0  | 1100 | 1.1269          | 45.9978 | 35.4045 | 45.0441 | 45.5143   | 18.58   |
| 0.8177        | 23.0  | 1150 | 1.1262          | 46.4454 | 35.5758 | 45.2515 | 45.9166   | 18.6    |
| 0.8106        | 24.0  | 1200 | 1.1346          | 46.832  | 36.0949 | 45.6135 | 46.2461   | 18.57   |
| 0.8059        | 25.0  | 1250 | 1.1327          | 46.671  | 35.6064 | 45.2941 | 45.8531   | 18.59   |
| 0.8057        | 26.0  | 1300 | 1.1351          | 46.7609 | 36.0229 | 45.4674 | 46.0057   | 18.56   |
| 0.7955        | 27.0  | 1350 | 1.1370          | 46.7472 | 35.6042 | 45.3153 | 46.0073   | 18.59   |
| 0.8           | 28.0  | 1400 | 1.1345          | 46.416  | 35.503  | 45.1255 | 45.6751   | 18.58   |
| 0.7947        | 29.0  | 1450 | 1.1326          | 46.4454 | 35.4164 | 45.143  | 45.8219   | 18.59   |
| 0.7966        | 30.0  | 1500 | 1.1346          | 46.4472 | 35.46   | 45.1554 | 45.8231   | 18.59   |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.10.1
- Datasets 2.10.1
- Tokenizers 0.13.2
