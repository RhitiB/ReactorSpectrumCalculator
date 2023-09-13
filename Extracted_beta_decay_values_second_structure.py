import os
os.chdir(r"D:\Python_2\ENDF_FILE_READER\239Pu")
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import quad
import math
import numpy as np

#%%
input_file = r"D:\Python_2\ENDF_FILE_READER\Elements_Matched_Data_1.txt"
output_file = "Extracted_Elements_Beta_Decay_data_1.txt"
start_extraction = False
target_line_1 = "1.000000+0 1.000000+0"
target_line_2 = "1.000000+0 2.000000+0"
found_target_1 = False
found_target_2 = False
prev_to_target_line_1 = None
prev_to_target_line_2 = None

#%%
with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
    prev_line = None

    for line in file_in:
        if line.startswith("Sect ID: "):
            sect_id = line.strip().split(":")[1].strip()
            file_out.write("\nSect ID: " + sect_id + "\n")
        elif line.startswith("Element Name: "):
            element_name = line.strip().split(":")[1].strip()
            file_out.write("Element Name: " + element_name + "\n")
        elif line.startswith("Element Data:"):
            element_data = line.strip().split(":")[1].strip()
            # Replace plus and minus signs with "E" in the element_data
            element_data = element_data.replace('+', 'E').replace('-', 'E')
            file_out.write("Element Data: " + element_data + "\n")

        if not start_extraction:
            if target_line_1 in line:
                if found_target_1:
                    # Extract the 3rd and 4th elements from the target line
                    target_elements = line.strip().split()[2:4]
                    target_elements = [element.replace('+', 'e').replace('-', 'e') for element in target_elements]

                    if prev_to_target_line_1:
                        prev_line_elements = prev_to_target_line_1.strip().split()
                        if len(prev_line_elements) >= 2:
                            # Replace plus and minus signs with "E" in the elements
                            prev_line_elements[0] = prev_line_elements[0].replace('+', 'e').replace('-', 'e')
                            prev_line_elements[1] = prev_line_elements[1].replace('+', 'e').replace('-', 'e')

                            # Write the 1st, 2nd, 3rd, and 4th elements to the output file
                            file_out.write(prev_line_elements[0] + " " + prev_line_elements[1] + " ")
                            file_out.write(target_elements[0] + " " + target_elements[1] + "\n")

                found_target_1 = not found_target_1  # Toggle the flag after each occurrence
                prev_to_target_line_1 = prev_line  # Store the current line as the previous line for target_line_1

            if target_line_2 in line:
                if found_target_2:
                    # Extract the 3rd and 4th elements from the target line
                    target_elements = line.strip().split()[2:4]
                    target_elements = [element.replace('+', 'e').replace('-', 'e') for element in target_elements]

                    if prev_to_target_line_2:
                        prev_line_elements = prev_to_target_line_2.strip().split()
                        if len(prev_line_elements) >= 2:
                            # Replace plus and minus signs with "E" in the elements
                            prev_line_elements[0] = prev_line_elements[0].replace('+', 'e').replace('-', 'e')
                            prev_line_elements[1] = prev_line_elements[1].replace('+', 'e').replace('-', 'e')

                            # Write the 1st, 2nd, 3rd, and 4th elements to the output file
                            file_out.write(prev_line_elements[0] + " " + prev_line_elements[1] + "\n")
                            file_out.write(target_elements[0] + " " + target_elements[1] + "\n")

                found_target_2 = not found_target_2  # Toggle the flag after each occurrence
                prev_to_target_line_2 = prev_line  # Store the current line as the previous line for target_line_2

        elif found_target_1 or found_target_2:
            file_out.write(line)

        prev_line = line