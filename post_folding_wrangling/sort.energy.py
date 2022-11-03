import sys
import os
import time
import pandas as pd

input_file = sys.argv[1] 

#pd.read_csv(myfile,sep='\t',skiprows=(0,1,2),header=(0))



df = pd.read_csv(input_file, sep='\s+', header=1) 

print(df)

#df = df.sort_values('

#print(df)