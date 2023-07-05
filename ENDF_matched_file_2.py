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

#Print the combined elements
#print(element_names)

#%%

'''Printing the data of the matching elements'''

'''with open ("ENDF_FILE_READER_1.txt", "r") as file1:
    content=file1.read().replace(" ", "")
    for element in element_names:
        if element.replace(" ", "")in content:
            print(f"Element'{element}' found in the text file")'''
        #%%
'''with open ("ENDF_FILE_READER_2.txt", "r") as file1:
    content=file1.read().replace(" ", "")
    for element in element_names:
        if element.replace(" ", "")in content:
            
            print(f"Element'{element}' found in the text file") 
            
            #%%
    with open ("ENDF_FILE_READER_3.txt", "r") as file1:
    content=file1.read().replace(" ", "")
    for element in element_names:
        if element.replace(" ", "")in content:
            print(f"Element'{element}' found in the text file") '''            

#%%

with open("ENDF_FILE_READER_1.txt", "r") as file1:
    lines = file1.readlines()
    for element in element_names:
        element = element.replace(" ", "")
        if element.endswith("-M"):
            element_without_m = element.replace("-M", "M")
            found = False
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element_without_m in line_without_spaces:
                    sectId_index = i - 5  
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        print(f"{sectId}")
                        print(f"Element Name: {element}")
                    found = True
                    continue
            
        else:
            found = False
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        print(f"{sectId}")
                        print(f"Element Name: {element}")
                    found = True
                    break
            
#%%
output_file = "Elements Matched Data_1.txt"  # Name of the output file

with open("ENDF_FILE_READER_1.txt", "r") as file1, open(output_file, "w") as file_out:
    lines = file1.readlines()
    for element in element_names:
        element = element.replace(" ", "")
        found = False  # Flag to track if element is found
        printed = False  # Flag to track if element is already printed
        sectId = ""  # Initialize sectId to an empty string
        if element.endswith("-M"):
            element_without_m = element.replace("-M", "M")
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element_without_m in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        found = True
                        break
        else:
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        found = True
                        break
        if found:
            file_out.write(f"Sect ID: {sectId}\n")
            file_out.write(f"Element Name: {element}\n")
            
            
#%%

with open("ENDF_FILE_READER_2.txt", "r") as file1:
    lines = file1.readlines()
    for element in element_names:
        element = element.replace(" ", "")
        if element.endswith("-M"):
            element_without_m = element.replace("-M", "M")
            found = False
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element_without_m in line_without_spaces:
                    sectId_index = i - 5  
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        print(f"{sectId}")
                        print(f"Element Name: {element}")
                    found = True
                    continue
            
        else:
            found = False
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        print(f"{sectId}")
                        print(f"Element Name: {element}")
                    found = True
                    break
#%%
                
output_file = "Elements Matched Data_2.txt"  # Name of the output file

with open("ENDF_FILE_READER_2.txt", "r") as file1, open(output_file, "w") as file_out:
    lines = file1.readlines()
    for element in element_names:
        element = element.replace(" ", "")
        found = False  # Flag to track if element is found
        printed = False  # Flag to track if element is already printed
        sectId = ""  # Initialize sectId to an empty string
        if element.endswith("-M"):
            element_without_m = element.replace("-M", "M")
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element_without_m in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        found = True
                        break
        else:
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        found = True
                        break
        if found:
            file_out.write(f"Sect ID: {sectId}\n")
            file_out.write(f"Element Name: {element}\n")

            

#%%


output_file = "Elements Matched Data_3.txt"  # Name of the output file

with open("ENDF_FILE_READER_3.txt", "r") as file1, open(output_file, "w") as file_out:
    lines = file1.readlines()
    for element in element_names:
        element = element.replace(" ", "")
        found = False  # Flag to track if element is found
        printed = False  # Flag to track if element is already printed
        sectId = ""  # Initialize sectId to an empty string
        if element.endswith("-M"):
            element_without_m = element.replace("-M", "M")
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element_without_m in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        found = True
                        break
        else:
            for i in range(len(lines)):
                line_without_spaces = lines[i].replace(" ", "")
                if element in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines[sectId_index].strip()
                        found = True
                        break
        if found:
            file_out.write(f"Sect ID: {sectId}\n")
            file_out.write(f"Element Name: {element}\n")