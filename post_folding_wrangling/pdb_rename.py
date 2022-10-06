# renames all of the pdbs based on the base name. 

import sys
import os
import time
import colorama
from colorama import Fore
from datetime import datetime, timedelta

import shutil

# Look for output/input 


if len(sys.argv) < 1:
    print(Fore.RED + "What's going on here buddy?\nYou need to give me a name...\nplease")
    time.sleep(.5)    
    exit() 

if sys.argv[1][0] != '/' or sys.argv[1][-1] != '/':
    print(Fore.RED + 'ERROR: Just a reminder. directories should have a slash "/" before and after the path. Make sure you included that or it won\'t work ')
    time.sleep(.5)
    exit() 


folder = sys.argv[1]

current_path = os.path.abspath(os.getcwd())

output_name = "output"

new_folder = os.path.join(current_path,output_name)
if not os.path.exists(new_folder):
    os.mkdir(new_folder)

for path, subdirs, files in os.walk(folder):
    for name in files:
        #print(os.path.join(path, name))
        print(name)
        if name == "ranked_0.pdb":
            print(name)
            base_name = os.path.basename(path)
            shutil.copy2(os.path.join(os.path.join(path, name)),new_folder)
            os.rename(os.path.join(new_folder, "ranked_0.pdb"),os.path.join(new_folder,base_name+".pdb"))
