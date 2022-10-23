#! /bin/bash


source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
./run.sh -d /home/haryu/alphafoldDownload -o /home/icanders/alphafold_output/ -m model_1 -f /home/icanders/MSH6_tudor/Musa_acuminata.fasta -t $(date +'%Y-%m-%d')
sleep 60 # just to be kind to the scheduler
done

