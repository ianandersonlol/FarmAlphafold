#!/bin/bash -l
#SBATCH -o /home/test/slurm-log/27787_output.txt
#SBATCH -e /home/test/slurm-log/27787_errors.txt
#SBATCH -J 27787_job
#SBATCH -t 48:00:00
#SBATCH -c 32
#SBATCH --mem 256G
#SBATCH --partition=bmh
#SBATCH --mail-type=ALL
#SBATCH --mail-user=test
set -e
set -u
module load spack/singularity/3.8.3
singularity instance start -B /home/haryu/alphafoldDownload /home/icanders/alphafold.sif bash
singularity exec instance://bash ~/27787.sh
