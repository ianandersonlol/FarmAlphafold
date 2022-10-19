#!/bin/bash -l
#SBATCH -o /home/ierwerwere/slurm-log/26229_output.txt
#SBATCH -e /home/ierwerwere/slurm-log/26229_errors.txt
#SBATCH -J 26229_job
#SBATCH -t 48:00:00
#SBATCH -c 32
#SBATCH --mem 256G
#SBATCH --partition=bmh
#SBATCH --mail-type=ALL
#SBATCH --mail-user=werw@dgjr.com
set -e
set -u
module load spack/singularity/3.8.3
singularity instance start -B /home/haryu/alphafoldDownload /home/icanders/alphafold.sif bash
singularity exec instance://bash ~/26229.sh

