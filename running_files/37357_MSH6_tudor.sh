#! /bin/bash

source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
for FILE in /home/icanders/MSH6_tudor/*.fasta; do
	echo ${FILE} 
	out="$(basename ${FILE} .fasta)"
	if [ ! -f "/home/icanders/alphafoldtestoutput/MSH6_tudor$out/ranked_0.pdb" ]; then
		 echo ${FILE} "Doesn't exist... folding" then
		./run.sh -d /home/icanders/alphafoldDownload -o /home/icanders/alphafoldtestoutput/MSH6_tudor/ -m model_1 -f "${FILE}" -t 2023-01-06
		sleep 60 # just to be kind to the scheduler
	fi
done

