import random
import sys
import os
from Bio import SeqIO

def mutate_protein(protein_fasta):
    # Split the FASTA file into the header and the sequence
    for record in SeqIO.parse(protein_fasta, 'fasta'):
    # Get the header and sequence from the record
        header = record.id
        sequence = str(record.seq)


    # Choose a random point in the sequence to mutate
    mutation_point = random.randint(0, len(sequence) - 1)

    # Create a list of all the amino acids, with the exception of the one at the mutation point
    amino_acids = list(sequence)
    del amino_acids[mutation_point]
    all_amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    # Choose a new amino acid at random
    new_amino_acid = random.choice(all_amino_acids)

    # Insert the new amino acid into the sequence
    sequence = sequence[:mutation_point] + new_amino_acid + sequence[mutation_point + 1:]

    # Create the new FASTA file with the mutated sequence
    mutated_fasta = f">{header}_1\n{sequence}"

    return mutated_fasta

# Get the original protein FASTA from the command line arguments
if __name__ == "__main__":
    
    protein_fasta = sys.argv[1]
    output_dir = sys.argv[2]
    if sys.argv[3]:
        count = int(sys.argv[3])
    else:
        count = 500
    # Split the header and the sequence
    if '\n' in protein_fasta:
        header, sequence = protein_fasta.strip().split('\n', 1)
    else:
        header = protein_fasta.strip()
        sequence = ''


    # Get the base name of the original FASTA file
    base_name = os.path.splitext(os.path.basename(protein_fasta))[0]

    # Initialize a list to store the mutated FASTA files
    mutated_fastas = []

    # Mutate the protein n times
    while len(mutated_fastas) < count:
        # Mutate the protein
        mutated_fasta = mutate_protein(protein_fasta)

        # Add the mutated FASTA to the list, but only if it is unique
        if mutated_fasta not in mutated_fastas:
            mutated_fastas.append(mutated_fasta)

    # Save the mutated FASTA files to disk
    for i, mutated_fasta in enumerate(mutated_fastas):
        file_path = os.path.join(output_dir, f"{base_name}_{i+1}.fasta")
        with open(file_path, 'w') as f:
            f.write(mutated_fasta)
        print("Creating "+str(i)+" mutation")
    print(f"Created {len(mutated_fastas)} unique mutated FASTA files.")
