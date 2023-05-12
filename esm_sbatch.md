# ESMFOLD Script Documentation

This script is designed to run a Python script called `esm_create_bash.py` using the SLURM workload manager. It sets various SLURM options, such as job name, output and error log file paths, time limit, number of CPU cores, memory allocation, GPU usage, and email notification settings. The script takes two command line arguments, an input directory and an output directory, and passes them as arguments to the `esm_create_bash.py` Python script.

## Usage

To use this script, follow the steps below:

1. Ensure that you have SLURM installed and configured on your system.
2. Make sure that you have the necessary permissions to run SLURM jobs.
3. Prepare the input files required by the `esm_create_bash.py` script and place them in a directory of your choice.
4. Choose a directory where you want the output files to be saved.
5. Open a terminal or command prompt and navigate to the directory where this script is saved.
6. Execute the script using the `sbatch` command, providing the input and output directories as command line arguments.

Example usage:

```bash
sbatch esmfold_script.sh /path/to/input_directory /path/to/output_directory
```

Note: Replace /path/to/input_directory with the actual path to your input directory, and /path/to/output_directory with the desired output directory.

## SLURM Options
The following SLURM options are set in this script:

```bash
#!/bin/bash -l
#SBATCH -o /home/[directory]/slurm-log/ESM_folding.txt
#SBATCH -e /home/[directory]/slurm-log/ESM_folding_errors.txt
#SBATCH -J ESMFOLD
#SBATCH -t 48:00:00
#SBATCH -c 16
#SBATCH --mem 128G
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu-a100-h
#SBATCH --mail-type=ALL
#SBATCH --mail-user=[email]
```
`-o /home/[directory]/slurm-log/ESM_folding.txt`: Specifies the path where the standard output log file will be written.
`-e /home/[directory]/slurm-log/ESM_folding_errors.txt`: Specifies the path where the error log file will be written.
`-J ESMFOLD`: Sets the job name to "ESMFOLD".
`-t 48:00:00`: Sets the time limit for the job to 48 hours.
`-c 16`: Requests 16 CPU cores for the job.
`--mem 128G`: Requests 128GB of memory for the job.
`--gres=gpu:1`: Requests 1 GPU for the job.
`--partition=gpu-a100-h`: Specifies the GPU partition to run the job on.
`--mail-type=ALL`: Sends email notifications for job events.
`--mail-user=[youremail]`: Specifies the email address to receive notifications.

## Command Line Arguments
This script expects two command line arguments:

input_directory: The path to the directory containing the input files required by the esm_create_bash.py script.
output_directory: The path to the directory where the output files will be saved.
Ensure that you provide valid and existing directory paths as arguments.

## Disclaimer 
Using the Meta API only allows for proteins under 400AA. To do more, they must be run on the inhouse installation. See Evan. 

