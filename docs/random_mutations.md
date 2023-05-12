# Code Documentation

The code in this file is used to mutate a protein FASTA file and generate multiple mutated FASTA files. The mutations are created by randomly selecting an amino acid in the sequence and replacing it with another randomly selected amino acid. The mutated FASTA files are saved to a specified output directory.

## Dependencies

This script requires the following dependencies:
- `random`
- `sys`
- `os`
- `Bio` from `biopython`

## Functions

### `mutate_protein(protein_fasta)`

This function takes a protein FASTA file as input and returns a mutated FASTA file with a single amino acid substitution. The mutation is created by selecting a random amino acid in the sequence and replacing it with another randomly selected amino acid.

### Main Script

The main script of this program reads in the input protein FASTA file and output directory from command line arguments. It then generates a specified number of mutated FASTA files using the `mutate_protein` function and saves them to the specified output directory. The number of mutated FASTA files generated is either specified by the third command line argument or defaults to 500 if not provided.

## Command Line Arguments

This script requires the following command line arguments:
1. `protein_fasta`: the input protein FASTA file
2. `output_dir`: the output directory to save the mutated FASTA files
3. `count` (optional): the number of mutated FASTA files to generate. Defaults to 500 if not provided.

## Example Usage

```python
python mutate_protein.py input.fasta output_directory/ 100
```

This will mutate the protein sequences in `input.fasta` and generate 100 mutated FASTA files, which will be saved in the `output_directory/` directory.

```python
python mutate_protein.py input.fasta output_directory/
```

This will mutate the protein sequences in `input.fasta` and generate 500 mutated FASTA files (default value), which will be saved in the `output_directory/` directory.
