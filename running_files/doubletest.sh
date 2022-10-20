#! /bin/bash

source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
./run.sh -d /home/haryu/alphafoldDownload -o /home/icanders/alphafold_output -m model_1 -f /home/haryu/alphafold/proteins/Q0JH50.fasta -t 2022-11-03