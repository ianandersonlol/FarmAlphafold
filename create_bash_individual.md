# Script Documentation

This script takes in input arguments from the command line and generates two shell scripts, `file_name_individual.sh` and `file_name_initialize.sh`. It also prints some information to the console.

## Requirements
This script requires the following modules to be installed:
- sys
- os
- time
- colorama
- colorama.Fore

## Usage
To use this script, call it from the command line with the following arguments:
- output_dir: The directory to output files to
- input_path: The path to the input file
- email: Email address to send notifications to
- davis_id: The farm name to use in slurm_logs

```python
python create_bash_individual.py <output_dir> <input_path> <email> <davis_id>
```

## Output
This script generates two shell scripts:
- `file_name_individual.sh`: A shell script that runs the Alphafold program on the input file.
- `file_name_initialize.sh`: A shell script that initializes the Alphafold program.
