import sys
import os

# Look for output/input directories.

if len(sys.argv) == 1:
    print("What's going on here buddy?\nYou need to give me a name...\nplease")
    exit() 

if len(sys.argv) ==2:
    print("Ok boys,girls, and NBs\n We need to do both a an output director AND an input directory")
    exit()

if len(sys.argv) >3 :
    print("Woah there cowbow!\nThis is UNIX!\nLet's avoid spaces in directory names, shall we?\nDon't try to be smart by putting the whole thing in quotes either!")
    exit()


 
current_path = os.path.abspath(os.getcwd())

maindir = sys.argv[1]

if ' ' in maindir:
    print("Okay, look smart guy/gal/non-binary pal.\nThis is UNIX.\nYou REALLY shouldn't be putting spaces in your directory names!!!\nBE BETTER!")

newpath = os.path.join(current_path, maindir) 

print("Making directory and subdirectories for: {0}".format(maindir))

if not os.path.exists(newpath):
    print("{0} does not exist, making it.".format(maindir))
    os.makedirs(newpath)

def write_loop(output_dir,input_dir):
    o = open(input_dir+'_loop.sh', 'w')
    print('',file=o)
    print('singularity exec --nv -B /home/haryu/alphafoldDownload alphafold.sif bash')
    print('source /opt/miniconda3/etc/profile.d/conda.sh')
    print('conda activate alphafold')
    print('cd /opt/alphafold/')
    print('for FILE in *.fasta; do')
    print('echo $\{FILE}\ ')
    print('./run.sh -d /home/haryu/alphafoldDownload -o {0} -m model_1 -f {1}/{FILE}/ -t $(date +\'%Y-%m-\%d\ '):format(output_dir,input_dir)
    print('sleep 60 # just to be kind to the scheduler')
    print('done')
    print('',file=o)
    o.close()

write_loop(sys.argv[1],sys.argv[2])

