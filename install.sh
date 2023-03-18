#!/bin/bash

python3 -m venv ./Calvados_taskA_venv

source ./Calvados_taskA_venv/bin/activate

pip install -r requirements.txt

deactivate

wget https://unicloud.unicaen.fr/index.php/s/Pq562kaxabR433L/download/saved_models.tgz
tar -xvf ./saved_models.tgz
rm ./saved_models.tgz 