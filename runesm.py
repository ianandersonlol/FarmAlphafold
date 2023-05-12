# Script Documentation

This Python script automates the process of sending protein sequence data to the ESM Atlas API to fold the sequence, and saving the returned protein structure to a file. 

## Requirements

The script requires the following Python libraries:

- os
- sys
- subprocess
- time

These are standard libraries and should be pre-installed with Python.

## Usage

Run the script using the following command:

`python <script_name.py> <input_directory> <output_directory>`


Where:

- `<script_name.py>` is the name of this script.
- `<input_directory>` is the directory that contains the input FASTA files (.fasta or .fa).
- `<output_directory>` is the directory where output files will be saved.

Please replace `<...>` with your actual values. 

The script iterates through all the files in the provided input directory. If a file is a FASTA file (i.e., it ends with .fasta or .fa), the script reads the protein sequence from the file and sends it to the ESM Atlas API using a curl command. 

The response from the API, which is the folded protein structure in PDB format, is saved to a file in the provided output directory. The output file has the same name as the input file but with the extension .pdb.

Please make sure you have the necessary permissions to read files from the input directory and to create and write files in the output directory.
