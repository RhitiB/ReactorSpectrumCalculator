import os
os.chdir(r"D:\Python_2\ENDF_FILE_READER")
input_file = "Elements_Matched_Data_1.txt"
output_file = "Extracted_Elements_Beta_Decay_data_xxxxxx.txt"
n = 3  # Number of lines to skip at the end
lines_to_write = []
start_extraction = False
extraction_count = 0
#print("testeo")
with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
    for line in file_in:
        if line.startswith("Sect ID: "):
            if start_extraction:
                start_extraction = False
                extraction_count = 0
                # Write the extracted lines to the output file with the desired format
                for i, l in enumerate(lines_to_write):
                    if i % 1 == 0:  # Write the data and skip every other line (odd lines)
                        elements = l.strip().split()
                        formatted_columns = []
                        for col in elements[0:6]:
                            if '.' in col:
                                formatted_columns.append(col.rjust(18))
                            else:
                                formatted_columns.append(col.rjust(11))
                        formated_columns_final=(" ".join(formatted_columns)).strip().split()
                        #file_out.write(" ".join(formatted_columns) + "\n")
                        #print(formated_columns_final[0])
                        if (len(formated_columns_final) == 6):
                            file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                            file_out.write(formated_columns_final[2]+ "  " + formated_columns_final[3] + "\n")
                            file_out.write(formated_columns_final[4]+ "  " + formated_columns_final[5] + "\n")
                        elif (len(formated_columns_final) == 5):
                            file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                            file_out.write(formated_columns_final[2]+ "  " + formated_columns_final[3] + "\n")
                            file_out.write(formated_columns_final[4]+ "  " + "\n")
                        elif (len(formated_columns_final) == 4):
                            file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                            file_out.write(formated_columns_final[2]+ "  " + formated_columns_final[3] + "\n")
                        elif (len(formated_columns_final) == 3):
                            file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                            file_out.write(formated_columns_final[2]+ "  " + "\n")
                        elif (len(formated_columns_final) == 2):
                            file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                        elif (len(formated_columns_final) == 1):
                            file_out.write(formated_columns_final[0]+ "\n")
                file_out.write("\n")  # Add a new line between elements
                lines_to_write = []

            sect_id = line.strip().split(":")[1].strip()
            file_out.write("\nSect ID: " + sect_id + "\n")
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
        elif (extraction_count>1) and (extraction_count<3) and (line.startswith(" 0.000000+0")):
            extraction_count += 1

        if start_extraction and extraction_count == 2:
            lines_to_write.append(line)

    # Write the extracted lines to the output file for the last element
    if start_extraction and extraction_count == 2:
        for i, l in enumerate(lines_to_write):
            if i % 2 == 0:  # Write the data and skip every other line (odd lines)
                elements = l.strip().split()
                formatted_columns = []
                print(elements[0])
                for col in elements[0:6]:
                    if '.' in col:
                        formatted_columns.append(col.rjust(18))
                    else:
                        formatted_columns.append(col.rjust(11))
                formated_columns_final=(" ".join(formatted_columns)).strip().split()
                #file_out.write(" ".join(formatted_columns) + "\n")
                if (len(formated_columns_final) == 6):
                    file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                    file_out.write(formated_columns_final[2]+ "  " + formated_columns_final[3] + "\n")
                    file_out.write(formated_columns_final[4]+ "  " + formated_columns_final[5] + "\n")
                elif (len(formated_columns_final) == 5):
                    file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                    file_out.write(formated_columns_final[2]+ "  " + formated_columns_final[3] + "\n")
                    file_out.write(formated_columns_final[4]+ "  " + "\n")
                elif (len(formated_columns_final) == 4):
                    file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                    file_out.write(formated_columns_final[2]+ "  " + formated_columns_final[3] + "\n")
                elif (len(formated_columns_final) == 3):
                    file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
                    file_out.write(formated_columns_final[2]+ "  " + "\n")
                elif (len(formated_columns_final) == 2):
                    file_out.write(formated_columns_final[0]+ "  " + formated_columns_final[1] + "\n")
        #file_out.write(" ".join(joint_columns_1) + "\n")