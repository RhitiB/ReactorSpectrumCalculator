import re
import os
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time
import webbrowser
#%%
# Change the working directory to your desired path
os.chdir(r"D:\Python_2\ENDF_FILE_READER\235U")

# Define a function to write unmatched elements to a file
def write_unmatched_elements(output_file, unmatched_elements):
    with open(output_file, "w") as file_out:
        for element in unmatched_elements:
            file_out.write(f"Element Name: {element}\n")
            file_out.write("Element Data: Not Found\n\n")

# Appending the element names to the list element_names
with open("Cum_Fission_235U.txt", "r") as file1:
    element_names = []
    for line in file1:
        columns = line.split()
        first_column = columns[0]
        first_column = re.sub(r'\s+', '-', first_column)
        element_names.append(first_column)
#%%
# Initialize a set to store matched elements
matched_elements = set()

# Loop through all three ENDF_READER text files
for file_number in range(1, 4):
    input_file = f"ENDF_FILE_READER_{file_number}.txt"
    output_file = f"Elements_Matched_Data_trial{file_number}.txt"

    with open(input_file, "r") as file1, open(output_file, "w") as file_out:
        lines1 = file1.readlines()
        id_counter = 0

        for element in element_names:
            element = element.replace(" ", "")
            found = False
            sectId = ""

            if element.endswith("-M"):
                element_without_m = element.replace("-M", "M")
                for i in range(len(lines1)):
                    line_without_spaces = lines1[i].replace(" ", "")
                    if element_without_m in line_without_spaces:
                        sectId_index = i - 5
                        if sectId_index >= 0:
                            sectId = lines1[sectId_index].strip()
                            found = True
                            break
            else:
                for i in range(len(lines1)):
                    line_without_spaces = lines1[i].replace(" ", "")
                    if element in line_without_spaces:
                        sectId_index = i - 5
                        if sectId_index >= 0:
                            sectId = lines1[sectId_index].strip()
                            found = True
                            break

            if found:
                sect_id_numeric = re.findall(r'\d+', sectId)[0]
                sect_id_numeric = int(sect_id_numeric)
                if sect_id_numeric % 2 == 1:
                    print(sect_id_numeric)
                    file_out.write(f"{sectId}\n")
                    file_out.write(f"Element Name: {element}\n")
                    matched_elements.add(element)  # Add the matched element to the set

                if (sect_id_numeric + 1) % 2 == 0:
                    print(sect_id_numeric + 1)
                    file_out.write(f"Element Data:{sect_id_numeric + 1}\n")
                    next_sect_id_lines = []
                    for i in range(lines1.index("Sect ID: " + str(sect_id_numeric + 1) + "\n") + 1, len(lines1)):
                        line = lines1[i]
                        if line.strip() == "":
                            break
                        next_sect_id_lines.append(line)
                    file_out.writelines(next_sect_id_lines)
                file_out.write("\n")

# Write unmatched elements to a separate output file
unmatched_elements = set(element_names) - matched_elements
write_unmatched_elements("Unmatched_Elements_235U.txt", unmatched_elements)
print("--------------------Finished----------------------------")
