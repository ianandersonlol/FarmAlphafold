# renames all of the pdbs based on the base name. 

import sys
import os
import time
import colorama
from colorama import Fore
from datetime import datetime, timedelta
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

current_path = os.path.abspath(sys.argv[1])

print(sys.argv[1])
print(os.path.basename(sys.argv[1]))


for count, filename in enumerate(os.listdir(folder)):
    dst = f"Hostel {str(count)}.pdb"
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
    
    #print("old filename is "+src+". New filename is "+dst)
    #os.rename(src, dst)
 
