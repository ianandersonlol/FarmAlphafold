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

if sys.argv[1][0] != '/' or sys.argv[1][-1] == '/':
    print(Fore.RED + 'ERROR: Just a reminder. directories should have a slash "/" before and after the path. Make sure you included that or it won\'t work ')
    time.sleep(.5)
    exit() 

data_file = sys.argv[1]
print(data_file)


o = open(os.path.basename(os.path.normpath(sys.argv[1]))+'_alignment_data.csv', 'w')
print('reference, subject,alignment_score',file=o) 
print(Fore.BLUE + "I am wasting your time with prints like this for the aesthetics becuase I have a problem.")
time.sleep(1)
with open(data_file) as openfile:
    for line in openfile:
       s = line.split()
      # print(s)
       for i,j in enumerate(s):
          if j == "=":
              print(Fore.GREEN+ "Adding Alignment of {0} against {1}: alignment score of {2}".format(s[i-7][:-1],s[i-12][:-1],s[i+1][:-1]))  
              print(s[i-12],s[i-7],s[i+1][:-1],file=o)
              time.sleep(.25) #I hate myself but this looks cool.
o.close()


