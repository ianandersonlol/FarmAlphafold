#!/bin/bash -l
#SBATCH -o /home/icanders/slurm-log/alphafoldn8mem64-stdout-%j.txt
#SBATCH -e /home/icanders/slurm-log/alphafoldn8mem64-stderr-%j.txt
#SBATCH -J alphafoldRunn8mem64
#SBATCH -t 48:00:00
#SBATCH -n 8
#SBATCH --mem 64G
#SBATCH --partition=bmm
#SBATCH --mail-type=ALL
#SBATCH --mail-user=icanderson@ucdavis.edu
set -e
set -u
module load spack/singularity/3.8.3
singularity instance start -B /home/haryu/alphafoldDownload /home/icanders/alphafold.sif bash
singularity exec instance://bash ~/running_files/alphafold_test.sh