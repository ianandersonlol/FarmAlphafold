import sys
import os
import time
import colorama
from colorama import Fore
from datetime import datetime, timedelta
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
print(Fore.GREEN + 'Validation complete. You have a real path.')
time.sleep(1) #Again, I hate myself. Why am I like this?

#helpers
file_name = str(int(time.process_time()*1000000))
two_days_date = datetime.today().strftime('%Y-%m-%d') #+ timedelta(days=2)
current_path = os.path.abspath(os.getcwd())
#eohelpers
output_dir = os.path.basename(current_path)

print(Fore.GREEN + 'Generating Files With Name: '+file_name+'.txt')
o = open(file_name+'.txt', 'w')
print('srun -p bmm -t 48:00:00 --mem=256GB -n 1 -c 32 --pty bash -l',file=o)
print('module load spack/singularity/3.8.3',file=o)

print('singularity exec --nv -B /home/haryu/alphafoldDownload alphafold.sif bash',file=o)
print('source /opt/miniconda3/etc/profile.d/conda.sh',file = o)
print('conda activate alphafold',file = o)
print('cd /opt/alphafold/',file = o)
for file in os.listdir(current_path):
    filename = os.fsdecode(file)
    if filename.endswith(".fasta") or filename.endswith(".fa"):
        print('./run.sh -d /home/haryu/alphafoldDownload -o {0}{4}/ -m model_1 -f "{1}{2}" -t {3}'.format(sys.argv[1],sys.argv[2],filename,two_days_date,output_dir),file =o)
print('',file=o)
o.close()

time.sleep(1) #IAN STOP YOU MONSTER AESTHETICS ARE FOR THE WEAK
print(Fore.YELLOW + 'Complete!') #WHY ARE WE LOADING A MODULE JUST FOR A COLOR! IAN STOP.

#/Users/iananderson/Desktop/phycocosm_fasta_hits_msh6_tudor_seqs


#./run.sh -d /home/haryu/alphafoldDownload  -o home/icanders/ -m model_1 -f /home/icanders/fungi_MSH6/ENI10155.1.fasta -t 2022-9-26




#cd /home/icanders