#! /bin/bash

source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
for FILE in *.fasta; do
	echo ${FILE} 
	./run.sh -d /home/haryu/alphafoldDownload -o /home/icanders/alphafold_output/ -m model_1 -f "/home/icanders/msh6_tudor_phytozome/${FILE}" -t 2022-10-21
	sleep 60 # just to be kind to the scheduler
done

