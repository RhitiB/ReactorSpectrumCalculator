import re
import os
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time
import webbrowser

os.chdir(r"/home/rhiti/Desktop/python/95Y_corrected")
#%%
'''Appending the element names to the list element_names'''
with open("Cum_Fission_241Pu.txt", "r") as file1:
   element_names=[]
   for line in file1:
       columns = line.split()

        # Get the first column
       first_column = columns[0]

        # Add the first column to the list
       element_names.append(first_column.strip("/n"))

# Print the combined elements
print(element_names)

#%%

'''Printing the data of the matching elements'''

with open("ENDF_FILE_READER.txt") as file1:
    for chunk in iter(lambda: file1.read(4096), ''):
        #print(chunk)
        
        
        '''for element in element_names:
        # Step 4: Search for a match using regular expressions
          pattern = r'\b{}\b'.format(re.escape(element.replace('-', r'[- ]?').replace('-M', r'(-M)?')))
          if re.search(pattern, chunk):
                # Step 5: Perform the matching
                #print("Match found for element '{}'".format(element))   
                with open("output.txt", 'a') as output_file:
                    output_file.write("Match found for element '{}'\n".format(element))'''
                #%%
                
                
    
    with open('example.txt') as f:
    if 'blabla' in f.read():
        print("true")
    


with open('largeFile', 'r') as inF:
    for line in inF:
        if 'myString' in line:
            for line in inF:
                if 'sectid' in line:
                    line=line+1# do_something
    



