#! /bin/bash


source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
./run.sh -d /home/haryu/alphafoldDownload -o /home/ian/ -m model_1 -f /lol/fasta.fa -t $(date +'%Y-%m-%d')

