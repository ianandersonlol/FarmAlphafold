#!/bin/bash -l
#SBATCH -o /home/hi/slurm-log/fasta.lol_fold_output.txt
#SBATCH -e /home/hi/slurm-log/fasta.lol_fold_errors.txt
#SBATCH -J fasta.lol_fold_job
#SBATCH -t 48:00:00
#SBATCH -c 16
#SBATCH --mem 128G
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu-a100-h
#SBATCH --mail-type=ALL
#SBATCH --mail-user=hi@hi.com
set -e
set -u
module load spack/singularity/3.8.3
singularity instance start --nv -B /home/haryu/alphafoldDownload /home/icanders/alphafold.sif bash
singularity exec instance://bash //Users/iananderson/Desktop/FarmAlphafold/running_files/fasta.lol_fold_individual.sh
