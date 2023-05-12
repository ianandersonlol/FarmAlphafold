# Rename PDB Files

This script renames all the PDB files with the base name of their respective directories and moves them to an output folder.

## Usage

`python script.py [folder_path]`

- `folder_path`: The path of the folder containing the PDB files. The folder path should have a slash ("/") before and after the path.

## Dependencies

- colorama

## Description

1. Import required modules:

   - sys, os, time, shutil: Standard Python modules for working with the file system and command line arguments.
   - colorama: A module to add colors to the console output.
   - datetime: A module to work with dates and times.

2. Check if the script has received a folder path as a command line argument. If not, display an error message and exit the script.

3. Check if the folder path has a slash ("/") before and after the path. If not, display an error message and exit the script.

4. Set the current working directory and the output folder name. If the output folder does not exist, create it.

5. Iterate through the files in the given folder path:

   1. Find files with the name "ranked_0.pdb".
   2. Get the base name of the parent directory.
   3. Rename the file with the base name and move it to the output folder.

## Example

If the folder structure is as follows:

```
main_folder/
    folder1/
        ranked_0.pdb
    folder2/
        ranked_0.pdb
```

Running the script:

`python script.py /main_folder/`

The output folder will contain the renamed files:

```
output/
    folder1.pdb
    folder2.pdb
```
