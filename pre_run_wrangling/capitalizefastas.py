import os
import sys
from Bio import SeqIO

def capitalize_fasta_sequences(input_path, output_path):
    sequences = []
    for record in SeqIO.parse(input_path, "fasta"):
        # Capitalize the sequence
        record.seq = record.seq.upper()
        sequences.append(record)
        
    # Write back to a new fasta file
    SeqIO.write(sequences, output_path, "fasta")

# Get directory path from command line argument
if len(sys.argv) != 2:
    print("Usage: python script_name.py <path_to_directory>")
    sys.exit(1)

directory_path = sys.argv[1]

# Check if provided path is a directory
if not os.path.isdir(directory_path):
    print("The provided path is not a directory.")
    sys.exit(1)

# Iterate over all files in the specified directory
for filename in os.listdir(directory_path):
    if filename.endswith(".fasta"):
        input_file_path = os.path.join(directory_path, filename)
        output_file_path = os.path.join(directory_path, f"{filename}")
        
        print(f"Processing {filename}...")
        capitalize_fasta_sequences(input_file_path, output_file_path)
        print(f"{filename} has been processed and saved as {output_file_path}")

print("All files have been processed.")
