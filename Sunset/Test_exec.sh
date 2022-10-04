singularity exec --nv -B /home/haryu/alphafoldDownload alphafold.sif bash
source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
./run.sh -d /home/haryu/alphafoldDownload  -o home/icanders/ -m model_1 -f /home/icanders/fungi_MSH6/ENI10155.1.fasta -t 2022-9-23

cd /home/icanders