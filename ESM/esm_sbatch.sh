#!/bin/bash -l
#SBATCH -o /home/icanders/slurm-log/ESM_folding.txt
#SBATCH -e /home/icanders/slurm-log/ESM_folding_errors.txt
#SBATCH -J ESMFOLD
#SBATCH -t 48:00:00
#SBATCH -c 16
#SBATCH --mem 128G
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu-a100-h
#SBATCH --mail-type=ALL
#SBATCH --mail-user=icanderson@ucdavis.edu

# Get the input and output directories from the command line arguments
input_directory=$1
output_directory=$2

# Call the Python script with the input and output directories as arguments
python3 /home/icanders/esm_create_bash.py $input_directory $output_directory