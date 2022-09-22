# FarmAlphafold



Running farm on Alphafold 


To split fastas
use python packet `fastsasplit`

`pip instal fastasplit`

`fastasplit nameoffasta`

To Rename all FASTAs based on the sequence.

for f in *.fasta
    do
    f1=$(head -n1 "$f" | sed 's/^.//')
    mv -n "$f" "$f1.fasta"
    done
