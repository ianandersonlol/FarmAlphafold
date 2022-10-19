#!/bin/bash -l
#SBATCH -o /home/icanders/slurm-log/39059_output.txt
#SBATCH -e /home/icanders/slurm-log/39059_errors.txt
#SBATCH -J Alphafolding
#SBATCH -t 48:00:00
#SBATCH -c 32
#SBATCH --mem 256G
#SBATCH --partition=bmm
#SBATCH --mail-type=ALL
#SBATCH --mail-user=icanderson@ucdavis.edu
set -e
set -u
module load spack/singularity/3.8.3
singularity instance start -B /home/haryu/alphafoldDownload /home/icanders/alphafold.sif bash
singularity exec instance://bash ~/39059_msh6_tudor_phytozome.sh

