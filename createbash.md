# Script Documentation

This Python script is designed to generate two shell scripts based on user input, which is used to automate tasks related to a UNIX farm. The script requires four arguments: `output_dir`, `input_dir`, `email`, and `davis_id`. It checks the validity of the given input, and if it passes, the script will generate two shell scripts, each performing a series of tasks.

## Requirements

The script requires the following Python libraries:

- sys
- os
- time
- colorama

You can install the required libraries using pip:

`pip install colorama`


## Usage

Run the script using the following command:

`python <script_name.py> <output_dir> <input_dir> <email> <farm_id>`


Where:

- `<script_name.py>` is the name of this script.
- `<output_dir>` is the directory where output files will be stored. This must start and end with a `/`.
- `<input_dir>` is the directory from which input files will be read. This must start and end with a `/`.
- `<email>` is the email address to which logs will be sent.
- `<farm_id>` is the ID for the farm.

Please note that you should replace `<...>` with your actual values. 

The script checks for the correct number of arguments and gives relevant error messages if the arguments are not as expected. For example, if not enough arguments are provided, the script will output an error message and exit.

The directories provided as input and output directories are validated to ensure they are properly formatted (i.e., they should start and end with a `/`). The script will also generate an error message and exit if spaces are included in the directory names.

Once the input is validated, the script will generate two shell scripts:

1. An initialization script named `file_name_input_dir_name_initialize.sh`. This script sets up the running environment, loads necessary modules, and runs the second script inside a Singularity instance.

2. A loop script named `file_name_input_dir_name.sh`. This script iterates over all `.fasta` files in the input directory, checks if the corresponding output file exists in the output directory, and if not, it runs a command to generate the output file.

Where `file_name` is a unique identifier based on the process time when the script is run, and `input_dir_name` is the name of the input directory.

Please make sure you have the necessary permissions to create and execute scripts in the directory where you run this script.

## Disclaimer

The script includes multiple `time.sleep()` commands for aesthetic purposes, because I am a queen. This might slightly slow down the script execution but should not affect its functionality.
