#! /bin/bash

source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
for FILE in /home/icanders/msh6_tudor_phytozome/*.fasta; do
	echo ${FILE} 
	./run.sh -d /home/haryu/alphafoldDownload -o /home/icanders/alphafold_output/ -m model_1 -f "${FILE}" -t 2022-10-27
	sleep 60 # just to be kind to the scheduler
done

