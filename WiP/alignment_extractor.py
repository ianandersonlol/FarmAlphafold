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
with open(data_file) as openfile:
    for line in openfile:
       s = line.split()
      # print(s)
       for i,j in enumerate(s):
          if j == "=":
              print(s[i-7],s[i+1])