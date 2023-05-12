# FASTA File Splitter Script Documentation

This script is a simple shell script to split a given FASTA file into multiple smaller FASTA files and then rename them based on the sequence.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Code Explanation](#code-explanation)

## Requirements

- Bash
- Python with pip

## Usage

To use this script, run the following command:

```sh
./script.sh <nameoffasta>
```

Replace `<nameoffasta>` with the name of your FASTA file.

## Code Explanation

1. Check if an argument is provided:

```sh
if [ $# -eq 0 ]
  then
    echo "No arguments provided. Usage: ./script.sh <nameoffasta>"
    exit 1
fi
```

This part of the script checks if any argument is provided. If no arguments are provided, it will display an error message and exit the script.

2. Install split-fasta if not already installed:

```sh
pip install split-fasta
```

This command installs the `split-fasta` Python package if it is not already installed.

3. Split the fasta file:

```sh
fastasplit $1
```

This part of the script uses the `fastasplit` command to split the input FASTA file into multiple smaller FASTA files.

4. Rename all FASTAs based on the sequence:

```sh
for f in *.fasta
do
    f1=$(head -n1 "$f" | sed 's/^.//')
    mv -n "$f" "$f1.fasta"
done
```

This loop iterates through each of the newly created FASTA files and renames them based on their sequence. It does this by extracting the first line of the file (which contains the sequence identifier) and then removing the `>` symbol using the `sed` command. Finally, it renames the file using the `mv` command.