import pandas
import os 
import time
from Bio import SeqIO
import sys


def parse_fasta(fname):
    identifiers = []
    with open(fname, "r") as fh:
        for line in fh:
            if not line.startswith(">"):
                identifiers.append(line)
    return identifiers

fasta_file = sys.argv[1]

print(parse_fasta(fasta_file))

