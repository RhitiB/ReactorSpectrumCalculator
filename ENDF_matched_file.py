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
element_names = []
pattern1 = r'\d+-[A-Za-z]+-\s+\d+'  # First pattern
pattern2 = r'\d+-[A-Za-z]+-\d+(-[A-Za-z]+)?'  # Modified pattern

with open("Cum_Fission_241Pu.txt", "r") as inputfile:
    lines = inputfile.readlines()

for line in lines:
    if line.strip():
        match1 = re.search(pattern1, line)
        match2 = re.search(pattern2, line)
        if match1:
            element_name1 = match1.group(0).replace('- ', '-')
            element_names.append(element_name1)
        if match2:
            element_name2 = match2.group(0).replace('- ', '-')
            element_names.append(element_name2)
element_names_mod=[]
# Print the elements as a column
for element in element_names:
    #print(element)
    element_names_mod.append(element)
print('\n'.join(element_names_mod))

#print(type(element_names_mod))






#%%

