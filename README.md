# FarmAlphafold
(Note this only works for people in the gmonroe group. Changes can be made to work on your group, just ask me.)

### Script Usage 

#### Alphafold
[running_files/create_bash.py](docs/createbash.md) This script automates the generation of alphafold slurm jobs for the Monroe lab farm account.

[running_files/srun_copy_paste.py](docs/srun_copy_paste.md) This script creates a text file with the command to startup an Srun and the lines you need to copy and paste to start folding everything in a directory. Nice if you want to watch it..

[running_files/create_bash_individual.py](docs/create_bash_individual.md) This script automates the generation of alphafold slurm jobs for the Monroe lab farm account for an individual fasta, instead of a directory of fastas like create_bash.

#### ESM 
[ESM/runesm.py](docs/runesm.md) This script submits protein sequences from FASTA files in a specified directory to the ESM Atlas API for structure prediction and saves the returned protein structures in a separate output directory.

[ESM/create_esm_bash.py](docs/create_esm_bash.md) This script, unlike the first one (createesm.py), names the output PDB files according to the first line in the corresponding FASTA file (excluding the '>' character), rather than the name of the input FASTA file.

[ESM/esm_sbatch.sh](docs/esm_sbatch.md)This script executes the esm_create_bash.py Python script using SLURM's sbatch command, passing input and output directories as arguments, while setting various SLURM options for job configuration.

#### Pre-fold tools

[pre_run_wranagling/random_mutations.py](docs/random_mutations.md) This script automatically generates a library of point mutations for a single protein sequence. 

[fastasplit.sh](docs/fastasplit.md) This script automatically splits up fastas with multiple proteins and renames the new files to have hte protein name. Note if the proteins all have the same name then it won't split htem proprly and will overlap. 

#### Post-fold tools
[post_fold_wrangling/pdb_rename.py](docs/pdb_rename.md) This script renames all the PDB files with the base name of their respective directories and moves them to an output folder.
