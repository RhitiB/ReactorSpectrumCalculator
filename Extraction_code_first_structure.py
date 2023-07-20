import os

os.chdir(r"U:/")
input_file = r"U:/Elements_Matched_Data_1.txt"
output_file = "Extracted_Elements_Beta_Decay_data_1_1.txt"

n = 3  # Number of lines to skip at the end

lines_to_write = []
start_extraction = False
extraction_count = 0

with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
    for line in file_in:
        if line.startswith("Sect ID: "):
            if start_extraction:
                start_extraction = False
                extraction_count = 0
                # Write the extracted lines to the output file
                file_out.writelines(lines_to_write[:-n])
                lines_to_write = []
            sect_id = line.strip().split(":")[1].strip()
            file_out.write("Sect ID: " + sect_id + "\n")
        elif line.startswith("Element Name: "):
            element_name = line.strip().split(":")[1].strip()
            file_out.write("Element Name: " + element_name + "\n")
        elif line.startswith("Element Data:"):
            element_data = line.strip().split(":")[1].strip()
            file_out.write("Element Data: " + element_data + "\n")
            extraction_count = 0  # Reset extraction_count when "Element Data" is found
        elif line.startswith(" 2.500000+3"):
            if extraction_count == 1:
                start_extraction = True
            extraction_count += 1

        if start_extraction and extraction_count < 3:
            lines_to_write.append(line)

    # Write the extracted lines to the output file for the last element
    if start_extraction and extraction_count == 2:
        file_out.writelines(lines_to_write[:-n])


        
                
                
    

