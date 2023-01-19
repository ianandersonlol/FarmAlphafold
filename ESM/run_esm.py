import os
import sys
import subprocess
from time import sleep
# Get the input and output directory paths from the command line arguments
input_directory = sys.argv[1]
output_directory = sys.argv[2]

# Iterate through all files and directories in the input directory
for root, dirs, files in os.walk(input_directory):
    # Iterate through all files in the current directory
    for filename in files:
        print(filename)
        
        filepath = os.path.join(root, filename)

        # Check if the file is a FASTA file
        if not filepath.endswith(".fasta") and not filepath.endswith(".fa"):
            continue

        # Open the FASTA file and read the name and data
        with open(filepath, "r") as fasta_file:
            name = fasta_file.readline().strip()[1:]  # Strip the first character from the name
            data = fasta_file.readline().strip()

        # Build the curl command
        command = ["curl", "-X", "POST", "--data", data, "https://api.esmatlas.com/foldSequence/v1/pdb/"]
        #sleep(2)
        print("Folding structure for..."+filename)
        # Run the curl command and save the output to a file in the output directory
        output_file = os.path.join(output_directory, filename + ".pdb")
        subprocess.run(command, stdout=open(output_file, "w"))