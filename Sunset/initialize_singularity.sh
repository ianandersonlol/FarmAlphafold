
#!/bin/bash -l
#SBATCH -o /home/icanders/slurm-log/alphafold_output.txt
#SBATCH -e /home/icanders/slurm-log/alphafold_errors.txt
#SBATCH -J AlphafoldRun
#SBATCH -t 48:00:00
#SBATCH -n 8
#SBATCH --mem 64G
#SBATCH --partition=bmh
#SBATCH --mail-type=ALL
#SBATCH --mail-user=icanderson@ucdavis.edu
set -e
set -u
module load spack/singularity/3.8.3
singularity instance start -B /home/haryu/alphafoldDownload /home/icanders/alphafold.sif bash
singularity exec instance://bash /home/icanders/run_alphafold.sh


