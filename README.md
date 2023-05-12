# FarmAlphafold
(Note this only works for people in the gmonroe group. Changes can be made to work on your group, just ask me.)


Running farm on Alphafold 


To split fastas
use python package `split-fasta`

`pip install split-fasta`

`fastasplit <nameoffasta>`

To Rename all FASTAs based on the sequence.

```
   for f in *.fasta
    do
    f1=$(head -n1 "$f" | sed 's/^.//')
    mv -n "$f" "$f1.fasta"
    done
```

On either the farm or your system, use the `create_bash.py` python script to generate your own files to run Sbatch. The script requires the following arguments `input directory` `output directory` `your email` and `your name on farm` Please surround the paths with slashes `/` If you don't the farm will yell at you, but don't worry, the script will yell at you. 

By default, it will reserve 32 cores and 256gb of ram. (I think 1cores:8gb ram is a good ratio for this, but you need to do at least 2 core 16gb) and on bmh. Once generated you can change this. 

### Script Usage 
#### Alphafold
[create_bash.py](docs/createbash.md) This script automates the generation of alphafold slurm jobs for the Monroe lab farm account.

[srun_copy_paste.py](docs/srun_copy_paste.md) This script creates a text file with the command to startup an Srun and the lines you need to copy and paste to start folding everything in a directory. Nice if you want to watch it..

[create_bash_individual.py](docs/create_bash_individual.md) This script automates the generation of alphafold slurm jobs for the Monroe lab farm account for an individual fasta, instead of a directory of fastas like create_bash.

#### ESM 
[runesm.py](docs/runesm.md) This script submits protein sequences from FASTA files in a specified directory to the ESM Atlas API for structure prediction and saves the returned protein structures in a separate output directory.

[create_esm_bash.py](docs/create_esm_bash.md) This script, unlike the first one (createesm.py), names the output PDB files according to the first line in the corresponding FASTA file (excluding the '>' character), rather than the name of the input FASTA file.

[esm_sbatch.sh](docs/esm_sbatch.md)This script executes the esm_create_bash.py Python script using SLURM's sbatch command, passing input and output directories as arguments, while setting various SLURM options for job configuration.

