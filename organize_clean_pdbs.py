# import required module
import os
import shutil
import sys

if len(sys.argv) >2:
    print("Only takes one optional argument. A directory. Otherwise uses current directroy. No idea what you're doing here.")
    exit()

# assign directory 
if len(sys.argv) == 2:
    current_path = os.path.normpath(sys.argv[1])
elif len(sys.argv) == 1:
    current_path = os.path.abspath(os.getcwd())

# iterate over files in that directory
for filename in os.listdir(current_path):
    if filename.endswith(".pdb"):        
        new_dir = os.path.basename(filename[:-4])
        new_path = os.path.join(current_path, new_dir)
        #print(new_path)
        if not os.path.exists(new_path):
            os.mkdir(new_path)
            print('combined pdbs folder not found...creating...')
        shutil.move(os.path.join(os.path.join(current_path, filename)),os.path.join(new_path, filename))
        print("Moving "+filename+" to the output folder.")        

