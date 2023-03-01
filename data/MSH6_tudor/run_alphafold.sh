#! /bin/bash

source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/

for FILE in *.fasta; do
echo ${FILE}
echo ./run.sh -d /home/haryu/alphafoldDownload -o ~/alphafold_output/${FILE%.*}/data -m model_1 -f ~/${FILE} -t $(date +'%Y-%m-%d')
sleep 60 # just to be kind to the scheduler
done
