import sys
import os
import time
import colorama
from colorama import Fore
from datetime import datetime, timedelta
# Look for output/input 
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

import pandas as pd

if len(sys.argv) < 1:
    print(Fore.RED + "What's going on here buddy?\nYou need to give me a name...\nplease")
    time.sleep(.5)    
    exit() 

if sys.argv[1][0] != '/' or sys.argv[1][-1] == '/':
    print(Fore.RED + 'ERROR: Just a reminder. directories should have a slash "/" before and after the path. Make sure you included that or it won\'t work ')
    time.sleep(.5)
    exit() 

data_file = sys.argv[1]
print(data_file)
alignment_temp_file = os.path.basename(os.path.normpath(sys.argv[1]))+'_alignment_score_temporary_file.csv'
atom_distance_temp_file = os.path.basename(os.path.normpath(sys.argv[1]))+'_atom_counts_temporary_file.csv'


o = open(alignment_temp_file, 'w')
print('reference, subject,alignment_score',file=o) 
with open(data_file) as openfile:
    for line in openfile:
       s = line.split()
      # print(s)
       for i,j in enumerate(s):
          if j == "=":
              print(Fore.GREEN+ "Adding Alignment of {0} against {1}: alignment score of {2}".format(s[i-7][:-1],s[i-12][:-1],s[i+1][:-1]))  
              print(s[i-12],s[i-7],s[i+1][:-1],file=o)
              time.sleep(.1) #I hate myself but this looks cool.
o.close()


o = open(atom_distance_temp_file, 'w')
print('npruned, pruned_distance,ntotal,total_distance',file=o) 
with open(data_file) as openfile:
    for line in openfile:
       s = line.split()
      # print(s)
       for i,j in enumerate(s):
          if j == "RMSD":
              print(Fore.GREEN+ "Adding Pruned Atoms {0} Armstrongs {1} total atoms {2} armstrongs {3}".format(s[i+2],s[i+7],s[i+11],s[i+13][:-2]))  
              print(s[i+2]+",",s[i+7]+", ",s[i+11]+", ",s[i+13][:-2],file=o)
              time.sleep(.1) #I hate myself but this looks cool.
o.close()


#I will admit this is a TERRIBLE way to do this, but it's all I know how to do :( 

alignment_data_frame = pd.read_csv(os.path.basename(os.path.normpath(sys.argv[1]))+'_alignment_score_temporary_file.csv')

atom_data_frame = pd.read_csv(os.path.basename(os.path.normpath(sys.argv[1]))+'_atom_counts_temporary_file.csv')


#concatable = [alignment_data_frame,atom_data_frame]

combined_dataframes = pd.concat([alignment_data_frame,atom_data_frame],axis = 1)
time.sleep(.2)

print('\n')
time.sleep(.075)
print('\n')
time.sleep(.075)


print(combined_dataframes)
combined_dataframes.to_csv(os.path.basename(os.path.normpath(sys.argv[1]))+'_alignment_data.csv')

os.remove(alignment_temp_file)
os.remove(atom_distance_temp_file)