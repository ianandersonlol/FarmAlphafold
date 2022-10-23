#!/bin/bash -l
#SBATCH -o /home/icanders/slurm-log/36483_output.txt
#SBATCH -e /home/icanders/slurm-log/36483_errors.txt
#SBATCH -J 36483_job
#SBATCH -t 48:00:00
#SBATCH -c 16
#SBATCH --mem 128G
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu-a100-h
#SBATCH --mail-type=ALL
#SBATCH --mail-user=icanderson@ucdavis.edu
set -e
set -u
module load spack/singularity/3.8.3
singularity instance start --nv -B /home/haryu/alphafoldDownload /home/icanders/alphafold.sif bash
singularity exec instance://bash ~/36483_individual.sh
