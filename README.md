# FarmAlphafold



Running farm on Alphafold 


To split fastas
use python package `fastsasplit`

`pip instal fastasplit`

`fastasplit nameoffasta`

To Rename all FASTAs based on the sequence.

```for f in *.fasta
    do
    f1=$(head -n1 "$f" | sed 's/^.//')
    mv -n "$f" "$f1.fasta"
    done
```

Use the `create_bash.py` python script to generate your own files to run Sbatch. The script requires the following arguments `input directory` `output directory` `your email` and `your name on farm` Please surround the paths with slashes `/` If you don't the farm will yell at you, but don't worry, the script will yell at you. 

By default, it will reserve 32 cores and 256gb of ram. (I think 1cores:8gb ram is good) and on bmh. Once generated you can change this. 
