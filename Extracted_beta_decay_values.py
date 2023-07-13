import re
import os
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time
import webbrowser

os.chdir(r"/home/rhiti/Desktop/python/95Y_corrected/Pu_241_Matched_elements")
#%%
# Specify the input and output file names
input_file = "Elements_Matched_Data_1.txt"
output_file = "Extracted_Elements_BetaDecay_Data_1.txt"

# Flag to indicate if we are in the second paragraph


# Open input and output files
with open(input_file, 'r') as file_in, open (output_file, "w") as file_out:
    start_extraction=False
    extraction_count=0
    for line in file_in:
        #print(lines)
        if line.startswith("Sect ID: "):
            sect_id=line.strip().split(":")[1].strip()
            #print("Sect ID:",sect_id)
            file_out.write("Sect ID: " + sect_id + "\n")
        if line.startswith("Element Name:"):
            element_name=line.strip().split(":")[1].strip()
            #print("Element Name:",element_name)
            file_out.write("Element Name:"+element_name + "\n")
        if line.startswith("Element Data:"):
            element_data=line.strip().split(":")[1].strip()
            #print("Element Data:",element_data)
            file_out.write("Element Data:" + element_data + "\n")
        
            
        
            
            
            
        
        
            
        
            
           
            

    
        