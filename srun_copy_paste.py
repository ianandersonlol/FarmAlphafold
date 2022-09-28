import sys
import os
import time
import colorama
from colorama import Fore
# Look for output/input 

if len(sys.argv) == 1:
    print(Fore.RED + "What's going on here buddy?\nYou need to give me a name...\nplease")
    time.sleep(.5)    
    exit() 
if len(sys.argv) ==2:
    print(Fore.RED + "Ok boys, girls, and NBs\n We need to do both a an output director AND an input directory")
    time.sleep(.5)
    exit()
if len(sys.argv) >3 :
    print(Fore.RED + "Woah there cowbow!\nThis is UNIX!\nLet's avoid spaces in directory names, shall we?\nDon't try to be smart by putting the whole thing in quotes either!")
    time.sleep(.5)
    exit()

print(os.path.basename(sys.argv[2]))

time.sleep(.5) # I hate myself for doing this. I just like it looking cool.

if sys.argv[1][0] != '/' or sys.argv[1][-1] != '/':
    print(Fore.RED + 'ERROR: Just a reminder. The farm needs your directories to have a slash "/" before and after the path. Make sure you included that or it won\'t work ')
    time.sleep(.5)
    exit() 

if sys.argv[2][0] != '/' or sys.argv[2][-1] != '/':
    print(Fore.RED + 'ERROR: Just a reminder. The farm needs your directories to have a slash "/" before and after the path. Make sure you included that or it won\'t work ')
    time.sleep(.5)
    exit()


srun -p bmh -t 4:00:00 --mem=128GB -n 1 -c 16 --pty bash -l
module load spack/singularity/3.8.3

singularity exec --nv -B /home/haryu/alphafoldDownload alphafold.sif bash
source /opt/miniconda3/etc/profile.d/conda.sh
conda activate alphafold
cd /opt/alphafold/
./run.sh -d /home/haryu/alphafoldDownload -o /home/icanders/alphafold_output -m model_1 -f /home/icanders/MSH6_tudor/Oryza_sativa.fasta -t 2022-09-27

./run.sh -d /home/haryu/alphafoldDownload  -o home/icanders/ -m model_1 -f /home/icanders/fungi_MSH6/ENI10155.1.fasta -t 2022-9-26




cd /home/icanders