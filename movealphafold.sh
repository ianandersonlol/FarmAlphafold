#!/bin/bash -l
#SBATCH -D /home/haryu/
#SBATCH -o /home/icanders/slurm-log/mover.txt
#SBATCH -e /home/icanders/slurm-log/movererrors.txt
#SBATCH -J alphafoldDownloadMove
#SBATCH -t 48:00:00
#SBATCH -n 1
#SBATCH --mem 32G
#SBATCH --partition=bmh
#SBATCH --mail-type=ALL
#SBATCH --mail-user=icanderson@ucdavis.edu

cp -r /home/haryu/alphafoldDownload /home/icanders/