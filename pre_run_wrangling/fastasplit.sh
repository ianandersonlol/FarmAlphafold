#!/bin/bash

# Check if argument is provided
if [ $# -eq 0 ]
  then
    echo "No arguments provided. Usage: ./script.sh <nameoffasta>"
    exit 1
fi

# Install split-fasta if not already installed
pip install split-fasta

# Split the fasta file
fastasplit $1

# Rename all FASTAs based on the sequence
for f in *.fasta
do
    f1=$(head -n1 "$f" | sed 's/^.//')
    mv -n "$f" "$f1.fasta"
done
