#! /bin/bash

source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
for FILE in /home/icanders/msh6_tudor_phytozome/*.fasta; do
	echo ${FILE} 
	out="$(basename ${FILE} .fasta)"
	if [ ! -f "/home/icanders/alphafold/output/msh6_tudor_phytozome$out/ranked_0.pdb" ]; then
		 echo ${FILE} "Doesn't exist... folding" then
		./run.sh -d /home/haryu/alphafoldDownload -o /home/icanders/alphafold/output/msh6_tudor_phytozome/ -m model_1 -f "${FILE}" -t 2022-11-03
		sleep 60 # just to be kind to the scheduler
	fi
done

