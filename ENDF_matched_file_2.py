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
output_file = "Elements Matched Data_1.txt"
with open("ENDF_FILE_READER_1.txt", "r") as file1, open(output_file, "w") as file_out:
    lines1 = file1.readlines()
    id_counter=0
    i=0
    for element in element_names:
        element = element.replace(" ", "")
        found = False  # Flag to track if element is found
        sectId = ""  # Initialize sectId to an empty string
        if element.endswith("-M"):
            element_without_m = element.replace("-M", "M")
            for i in range(len(lines1)):
                line_without_spaces = lines1[i].replace(" ", "")
                if element_without_m in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines1[sectId_index].strip()
                        found = True
                        break
        else:
            for i in range(len(lines1)):
                line_without_spaces = lines1[i].replace(" ", "")
                if element in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines1[sectId_index].strip()
                        found = True
                        break
        if found:
            sect_id_numeric = re.findall(r'\d+', sectId)[0]  # Extract numeric part of the sectId
            sect_id_numeric = int(sect_id_numeric)
            if sect_id_numeric % 2 == 1:  # Check if element ID is odd
                print(sect_id_numeric)
                file_out.write(f"{sectId}\n")
                file_out.write(f"Element Name: {element}\n")
            if (sect_id_numeric+1) % 2 == 0:  # Element data (even ID)
                print(sect_id_numeric+1)
                file_out.write(f"Element Data:{sect_id_numeric+1}\n")
                next_sect_id_lines = []
                for i in range(lines1.index("Sect ID: "+str(sect_id_numeric + 1)+"\n")+1, len(lines1)):
                    line = lines1[i]
                    if line.strip() == "":
                        break
                    next_sect_id_lines.append(line)
                file_out.writelines(next_sect_id_lines)
            file_out.write("\n")
            
print("--------------------Finished----------------------------")
            
            
            
            
            
            
               
                
#%%
                
output_file = "Elements Matched Data_2.txt"  # Name of the output file

with open("ENDF_FILE_READER_2.txt", "r") as file1, open(output_file, "w") as file_out:
    lines1 = file1.readlines()
    id_counter=0
    i=0
    for element in element_names:
        element = element.replace(" ", "")
        found = False  # Flag to track if element is found
        sectId = ""  # Initialize sectId to an empty string
        if element.endswith("-M"):
            element_without_m = element.replace("-M", "M")
            for i in range(len(lines1)):
                line_without_spaces = lines1[i].replace(" ", "")
                if element_without_m in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines1[sectId_index].strip()
                        found = True
                        break
        else:
            for i in range(len(lines1)):
                line_without_spaces = lines1[i].replace(" ", "")
                if element in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines1[sectId_index].strip()
                        found = True
                        break
        if found:
            sect_id_numeric = re.findall(r'\d+', sectId)[0]  # Extract numeric part of the sectId
            sect_id_numeric = int(sect_id_numeric)
            if sect_id_numeric % 2 == 1:  # Check if element ID is odd
                print(sect_id_numeric)
                file_out.write(f"{sectId}\n")
                file_out.write(f"Element Name: {element}\n")
            if (sect_id_numeric+1) % 2 == 0:  # Element data (even ID)
                print(sect_id_numeric+1)
                file_out.write(f"Element Data:{sect_id_numeric+1}\n")
                next_sect_id_lines = []
                for i in range(lines1.index("Sect ID: "+str(sect_id_numeric + 1)+"\n")+1, len(lines1)):
                    line = lines1[i]
                    if line.strip() == "":
                        break
                    next_sect_id_lines.append(line)
                file_out.writelines(next_sect_id_lines)
            file_out.write("\n")
            
print("--------------------Finished----------------------------")

            

#%%


output_file = "Elements Matched Data_3.txt"  # Name of the output file

with open("ENDF_FILE_READER_3.txt", "r") as file1, open(output_file, "w") as file_out:
    lines1 = file1.readlines()
    id_counter=0
    i=0
    for element in element_names:
        element = element.replace(" ", "")
        found = False  # Flag to track if element is found
        sectId = ""  # Initialize sectId to an empty string
        if element.endswith("-M"):
            element_without_m = element.replace("-M", "M")
            for i in range(len(lines1)):
                line_without_spaces = lines1[i].replace(" ", "")
                if element_without_m in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines1[sectId_index].strip()
                        found = True
                        break
        else:
            for i in range(len(lines1)):
                line_without_spaces = lines1[i].replace(" ", "")
                if element in line_without_spaces:
                    sectId_index = i - 5  # Assuming sectId is 4 lines before the element name
                    if sectId_index >= 0:
                        sectId = lines1[sectId_index].strip()
                        found = True
                        break
        if found:
            sect_id_numeric = re.findall(r'\d+', sectId)[0]  # Extract numeric part of the sectId
            sect_id_numeric = int(sect_id_numeric)
            if sect_id_numeric % 2 == 1:  # Check if element ID is odd
                print(sect_id_numeric)
                file_out.write(f"{sectId}\n")
                file_out.write(f"Element Name: {element}\n")
            if (sect_id_numeric+1) % 2 == 0:  # Element data (even ID)
                print(sect_id_numeric+1)
                file_out.write(f"Element Data:{sect_id_numeric+1}\n")
                next_sect_id_lines = []
                for i in range(lines1.index("Sect ID: "+str(sect_id_numeric + 1)+"\n")+1, len(lines1)):
                    line = lines1[i]
                    if line.strip() == "":
                        break
                    next_sect_id_lines.append(line)
                file_out.writelines(next_sect_id_lines)
            file_out.write("\n")
            
print("--------------------Finished----------------------------")
            
#%%            
          