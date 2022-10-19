import sys
import os
import time
import colorama
from colorama import Fore

from datetime import datetime, timedelta

# Look for output/input directories and email and davis ID 

print(os.path.basename(os.path.normpath(sys.argv[2])))

if len(sys.argv) == 1:
    print(Fore.RED + "What's going on here buddy?...You need to give me a name...please")
    time.sleep(.5)
    print(Fore.RED + "<output_dir>,<input_dir>,<email>,<davis_id>")
    time.sleep(.5)    
    exit() 

if len(sys.argv) ==2:
    print(Fore.RED + "Ok boys, girls, and enbys. We need to do both an output director AND an input directory")
    time.sleep(.5)
    print(Fore.RED + "<output_dir>,<input_dir>,<email>,<davis_id>")
    time.sleep(.5)
    exit()
if len(sys.argv) == 3:
    print(Fore.RED + 'You need to also give your e-mail address for logs')
    time.sleep(.5)
    print(Fore.RED + "<output_dir>,<input_dir>,<email>,<davis_id>")
    time.sleep(.5)
    exit()
if len(sys.argv) == 4:
    print(Fore.RED + 'You must aslo give me your farm name so we can put everything into your slurm_logs... Exiting...')
    time.sleep(.5)
    print(Fore.RED + "<output_dir>,<input_dir>,<email>,<davis_id>")
    time.sleep(.5)
    exit()
if len(sys.argv) >5 :
    print(Fore.RED + "Woah there cowbow! This is UNIX! Let's avoid spaces in directory names, shall we? Don't try to be smart by putting the whole thing in quotes either!")
    time.sleep(.5)
    print(Fore.RED + "<output_dir>,<input_dir>,<email>,<davis_id>")
    time.sleep(.5)
    exit()

print(Fore.GREEN+'Validating paths...')
time.sleep(.5) # I hate myself for doing this. I just like it looking cool.

if sys.argv[1][0] != '/' or sys.argv[1][-1] != '/':
    print(Fore.RED + 'ERROR: Just a reminder. The farm needs your directories to have a slash "/" before and after the path. Make sure you included that or it won\'t work ')
    time.sleep(.5)
    exit() 

if sys.argv[2][0] != '/' or sys.argv[2][-1] != '/':
    print(Fore.RED + 'ERROR: Just a reminder. The farm needs your directories to have a slash "/" before and after the path. Make sure you included that or it won\'t work ')
    time.sleep(.5)
    exit()


file_name = str(int(time.process_time()*1000000))

current_path = os.path.abspath(os.getcwd())

maindir = sys.argv[1]
two_days_date = datetime.today()+timedelta(days=2)
string_date = two_days_date.strftime('%Y-%m-%d')

if ' ' in maindir:
    print(Fore.RED + "Okay, look smart guy/gal/non-binary pal.\nThis is UNIX.\nYou REALLY shouldn't be putting spaces in your directory names!!!\nBE BETTER!")
    time.sleep(.5)
    exit()
newpath = os.path.join(current_path, maindir) 

print(Fore.GREEN + 'Validation complete. You have a real path.')
time.sleep(1) #Again, I hate myself. Why am I like this?  

def write_initialization():
    o = open(file_name+'_'+os.path.basename(os.path.normpath(sys.argv[2]))+'_initialize.sh', 'w')
    print('#!/bin/bash -l',file=o) 
    print('#SBATCH -o /home/'+sys.argv[4]+'/slurm-log/'+file_name+'_output.txt',file = o)
    print('#SBATCH -e /home/'+sys.argv[4]+'/slurm-log/'+file_name+'_errors.txt',file = o)
    print('#SBATCH -J Alphafolding',file = o)
    print('#SBATCH -t 48:00:00',file = o)
    print('#SBATCH -c 32',file = o)
    print('#SBATCH --mem 256G',file = o)
    print('#SBATCH --partition=bmm',file = o)
    print('#SBATCH --mail-type=ALL',file = o)
    print('#SBATCH --mail-user='+sys.argv[3],file = o)
    print('set -e',file = o)
    print('set -u',file = o)
    print('module load spack/singularity/3.8.3',file = o)
    print('singularity instance start -B /home/haryu/alphafoldDownload /home/icanders/alphafold.sif bash',file = o)
    print('singularity exec instance://bash ~/'+file_name+'_'+os.path.basename(os.path.normpath(sys.argv[2]))+'.sh',file = o)
    print('',file=o)
    o.close()

def write_loop(output_dir,input_dir):
    
    print(Fore.GREEN + 'Generating Files With Name: '+file_name+'_'+os.path.basename(os.path.normpath(sys.argv[2])))
    o = open(file_name+'_'+os.path.basename(os.path.normpath(sys.argv[2]))+'.sh', 'w')
    print('#! /bin/bash\n',file=o)
    print('source /opt/miniconda3/etc/profile.d/conda.sh', file = o)
    print('conda activate alphafold', file = o)
    print('cd /opt/alphafold/', file = o)
    print('for FILE in *.fasta; do',file = o)
    print('\techo ${FILE} ',file= o)
    print('\t./run.sh -d /home/haryu/alphafoldDownload -o {} -m model_1 -f "{}${{FILE}}" -t {}'.format(output_dir,input_dir,string_date),file = o)
    print('\tsleep 60 # just to be kind to the scheduler',file = o)
    print('done',file=o)
    print('',file=o)
    o.close()

write_loop(sys.argv[1],sys.argv[2])
write_initialization()

time.sleep(1) #IAN STOP YOU MONSTER AESTHETICS ARE FOR THE WEAK
print(Fore.YELLOW + 'Complete!') #WHY ARE WE LOADING A MODULE JUST FOR A COLOR! IAN STOP.