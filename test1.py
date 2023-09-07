import os
os.chdir(r"D:\Python_2\ENDF_FILE_READER")
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import quad
import math
import numpy as np
import pprint
#%%
input_file = "Elements_Matched_Data_1.txt"
output_file = "Extracted_Elements_Beta_Decay_data_xxx1_new.txt"
start_extraction = False
target_line_1 = "1.000000+0 1.000000+0"
target_line_2 = "1.000000+0 2.000000+0"
found_target_1 = False
found_target_2 = False
prev_to_target_line_1 = "Something"
prev_to_target_line_2 = "something"
prev_line = None
prev_line_elements = "something"
element_name = ""
target_elements = []
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
            #element_data = element_data.replace('+', 'E+').replace('-', 'E-')
            file_out.write("Element Data: " + element_data + "\n")

        if not start_extraction:
            if target_line_1 in line:
                found_target_1 = True
                target_elements = line.strip().split()[2:4]
                target_elements = [element.replace('+', 'e+').replace('-', 'E-') for element in target_elements]
                prev_to_target_line_1 = prev_line  # Store the line before the target line
                if prev_to_target_line_1:
                        prev_line_elements = prev_to_target_line_1.strip().split()
                        if len(prev_line_elements) >= 2:
                            # Replace plus and minus signs with "E" in the elements
                            prev_line_elements[0] = prev_line_elements[0].replace('+', 'E+').replace('-', 'E-')
                            prev_line_elements[1] = prev_line_elements[1].replace('+', 'E+').replace('-', 'E-')

                            # Write the 1st, 2nd, 3rd, and 4th elements to the output file
                file_out.write(prev_line_elements[0] + " " + prev_line_elements[1] + " ")
                file_out.write(target_elements[0] + " " + target_elements[1] + "\n")

                found_target_1 = not found_target_1  # Toggle the flag after each occurrence
                prev_to_target_line_1 = prev_line              
                
            #Condition for target line 2
        
            if target_line_2 in line:
                found_target_2 = True
                prev_to_target_line_2 = prev_line
                target_elements = line.strip().split()[2:4]
                #target_elements = [element.replace('+', 'e+').replace('-', 'e-') for element in target_elements]
                prev_to_target_line_2 = prev_line  # Store the line before the target line
            elif found_target_2:
                
                prev_line_elements = prev_to_target_line_2.strip().split()
                if len(prev_line_elements) >= 2:
                            # Replace plus and minus signs with "E" in the elements
                            prev_line_elements[0] = prev_line_elements[0].replace('+', 'E+').replace('-', 'E-')
                            prev_line_elements[1] = prev_line_elements[1].replace('+', 'E+').replace('-', 'E-')
                            target_elements[0] = target_elements[0].replace('+', 'E+').replace('-', 'E-')
                            target_elements[1] = target_elements[1].replace('+', 'E+').replace('-', 'E-')  
                            # Write the 1st, 2nd, 3rd, and 4th elements to the output file
                            file_out.write(prev_line_elements[0] + " " + prev_line_elements[1] + " "+ target_elements[0] + " " + target_elements[1] + "\n")

                found_target_2 = not found_target_2  # Toggle the flag after each occurrence
                prev_to_target_line_2 = prev_line  # Store the current line as the previous line for target_line_2
                
            elif found_target_1 or found_target_2:
                file_out.write(line)
            
        # Store the current line as the previous line for the next iteration'''
            prev_line = line

#%%
cum_yield_dict = {}  # Cumulative yield for all the elements from the mother isotope

# os.chdir("ENDF_FILE_READER")

with open("Cum_Fission_241Pu.txt", "r") as input_file1:
    for line in input_file1:
        columns = line.split()
        if len(columns) >= 4:
            isotope_name = columns[0]
            cum_yield_value = float(columns[3])
            
            element_name = isotope_name.split('-')[1]  # Extracting the element name
            
            if element_name not in cum_yield_dict:
                cum_yield_dict[element_name] = {}  # Creating a sub-dictionary if not already present
            
            cum_yield_dict[element_name][isotope_name] = cum_yield_value

# Print the resulting dictionary for verification

pprint.pprint(cum_yield_dict)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    
#%%
endpoints = []
BR = []
dict1 = {}
dictBR = {}  # Dictionary for Branching Ratios
with open("Extracted_Elements_Beta_Decay_data_xxx1_new.txt", "r") as input_file2:
    current_element_data = []
    current_BR_data = []
    element_name = None  # Initialize element_name
    
    for line in input_file2:
        line = line.strip("\n")
        if line.startswith("Sect ID: "):
            if current_BR_data:
                print("-----Current_BR_data--------")
                print(line)
                BR.append([value for value in current_BR_data])
                if element_name:
                    if str(element_name.split("-")[1]) not in dictBR:
                        dictBR[str(element_name.split("-")[1])] = {}
                    dictBR[str(element_name.split("-")[1])][element_name] = current_BR_data
                current_BR_data = []
            else:
                pass
        elif line.startswith("Element Name"):
            if current_element_data:
                print("-----Current_element_data--------")
                print(line)
                #element_name = line.strip().split(":")[1].strip()
                endpoints.append([value for value in current_element_data])
                if current_element_data and element_name:
                    if str(element_name.split("-")[1]) not in dict1:
                        dict1[str(element_name.split("-")[1])] = {}
                    dict1[str(element_name.split("-")[1])][element_name] = current_element_data
                current_element_data = []
            element_name = line.strip().split(":")[1].strip()
        elif line.startswith("Element Data: "):
            if current_element_data:
                endpoints.append([value for value in current_element_data])
        else:
            target_elements = line.strip().split()
            target_BR = line.strip().split()
            if len(target_elements) != 0:
                #print("-----Else--------")
                #print(line)
                endpoint = (float(target_elements[0]) / 1000)
                current_element_data.append(endpoint)
            if len(target_BR) != 0:
                br = float(target_BR[2])
                current_BR_data.append(br)
# Conditional for the last element:
if current_BR_data:
    print("-----Last element data--------")
    print(element_name)
    print(current_BR_data)
    if current_element_data and element_name:
        if str(element_name.split("-")[1]) not in dictBR:
            dictBR[str(element_name.split("-")[1])] = {}
        dictBR[str(element_name.split("-")[1])][element_name] = current_BR_data
if current_element_data and element_name:
    if str(element_name.split("-")[1]) not in dict1:
        dict1[str(element_name.split("-")[1])] = {}
    dict1[str(element_name.split("-")[1])][element_name] = current_element_data

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(dict1.get("Sr", "Key not found"))  # Check if 'Sr' key exists
print(len(dict1))
print(len(dictBR))
#%%                
#Finding the energy list and range of values
dict2 = {}

for key1 in dict1:
    for key2 in dict1[key1]:
        endpoints_sublist = []
        for value in dict1[key1][key2]:
            E_e = []
            int_value = int(value)  # Convert the value to an integer
            for x in range(int_value, -2, -1):
                E_e.append(value - x)
            endpoints_sublist.append(E_e)
        
        if key1 not in dict2:
            dict2[key1] = {}
            dict2[key1][key2] = endpoints_sublist
        else:
            dict2[key1][key2] = endpoints_sublist


#%%
#Finding the antineutrino energy range
dict3 = {}
for key1 in dict1:
    dict3[key1] = {}
    for key2 in dict1[key1]:
        new_sublist = []
        for i in range(len(dict1[key1][key2])):
            # Check if dict2[key1][key2][i] is an empty sequence
            if not dict2[key1][key2][i]:
                E_min_nu = 0  # Set a default value for E_min_nu
                E_max_nu = 0  # Set a default value for E_max_nu
            else:
                E_min_nu = dict1[key1][key2][i] - max(dict2[key1][key2][i])
                E_max_nu = dict1[key1][key2][i] - min(dict2[key1][key2][i])
            
            E_range = np.arange(E_min_nu, E_max_nu, 1)
            new_sublist.append(E_range.tolist())

        dict3[key1][key2] = new_sublist            
#%%
"""def integrand(E_o, E_nu):
    expr = (E_o - E_nu)**2 - 1
    if expr <= 0 or E_nu == 0 or E_o == E_nu:
        return 0
    
    denominator = math.sqrt(expr) * E_nu * 2 * (E_o - E_nu)
    if denominator.imag != 0:
        return 0
    else:
        return 1 / denominator.real

fixed_E_nu = 1.8 
normalization_constant_dict = {}

for key1 in dict1:
    normalization_constant_dict[key1] = {}
    
    for key2 in dict1[key1]:
        endpoints = dict1[key1][key2]
        E_anu_list = dict3[key1][key2]
        K_values = []
        
        for i in range(len(endpoints)):
            K_values_sublist = []
            
            for j in range(len(E_anu_list[i])):
                E_nu = E_anu_list[i][j]
                
                for E_o in endpoints:
                    # Call the integrand function and perform the integration
                    integration_result, _ = quad(integrand, E_o, float('inf'), args=(E_nu,))
                    K_values_sublist.append(integration_result)
                
                K_values.append(K_values_sublist)
        
        normalization_constant_dict[key1][key2] = K_values"""

#%%
phase_space_dict = {}
for key1 in dict1:
    phase_space_dict[key1] = {}  # Initialize a dictionary for each key in dict1
    for key2 in dict1[key1]:
        endpoints = dict1[key1][key2]
        E_anu_list = dict3[key1][key2]        
        phase_space = []        
        for i in range(len(endpoints)):
            phase_space_sublist = []
            for j in range(len(E_anu_list[i])):
                expr = (endpoints[i] - E_anu_list[i][j]) ** 2 - 1
                if expr < 0:
                    continue
                P = float(math.sqrt(expr) * (E_anu_list[i][j] ** 2) * (endpoints[i] - E_anu_list[i][j]))
                if endpoints[i] <= 0:
                    continue
                phase_space_sublist.append(P)            
            phase_space.append(phase_space_sublist)        
        phase_space_dict[key1][key2] = phase_space
        
#%%
#print("///////////////////////////////////////////////////////////////////////////////////////////////////////////")
#-----This is dn_dE calculation without normalization-----
dn_de_normalized_dict = {}
print("///////////////////////////////////////////////////////////////////////////////////////////////////////////")
for key1 in dict1:
    #print("########################################################################################################")
    #print(key1)
    #print(str(key1)+" has "+str(len(dict1[key1]))+ " elements")
    #print("cum_yield_dict key "+str(key1)+" has "+str(len(cum_yield_dict[key1]))+ " elements")
    dn_de_normalized_dict[key1] = {}
    for key2 in dict1[key1]:
        print("*************")
        if key2 not in dn_de_normalized_dict[key1]:
            dn_de_normalized_dict[key1][key2]=[]
        print(key2)
        #print(str(key2)+" has "+str(len(dict1[key1][key2]))+ " elements")
        if key1 in cum_yield_dict and key2 in cum_yield_dict[key1]:
            #print(dict1[key1][key2])
            #print("dict1[key1][key2] is a "+str(type(dict1[key1][key2])))
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            #print(cum_yield_dict[key1][key2])
            #print("cum_yield_dict[key1][key2] is a "+str(type(cum_yield_dict[key1][key2])))
            if key2 in dictBR.get(key1, {}):
                print("=============================================================================================")
                BR = dictBR[key1][key2]
                print("BR is"+str(dictBR[key1][key2]))
                C = cum_yield_dict[key1][key2]
                P = phase_space_dict[key1][key2]
                dn_dE_2 = []                
                if len(BR) == len(P):
                    for j in range(len(P)):
                        dn_dE_2 = []
                        if isinstance(C, (int, float)) and isinstance(BR[j], (int, float)):
                            for m in range(len(P[j])):
                                dn_dE_2.append(C * BR[j] * P[j][m])
                        elif not isinstance(C, (int, float)) and isinstance(BR[j], (int, float)) and isinstance(P[j], (int, float)):
                            print("Error: C is not a numerical value.")
                        elif isinstance(C, (int, float)) and not isinstance(BR[j], (int, float)) and isinstance(P[j], (int, float)):
                            print("Error: BR is not a numerical value.")
                        elif isinstance(C, (int, float)) and isinstance(BR[j], (int, float)) and not isinstance(P[j], (int, float)):
                            print("Error: P[j] is not a numerical value.")
                        #else:
                        #    print("Error: One of C, BR, or P[j] is not a numerical value.")
                        #    #print(f"C: {C}, BR[{j}]: {BR[j]}, P[{j}]: {P[j]}")

                        dn_de_normalized_dict[key1][key2].append(dn_dE_2)
                else:
                    print("Error: BR and P lists have different lengths.")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# print(len(phase_space_dict["Co"]["27-Co-66"]))
# print(len(dn_de_normalized_dict["Co"]["27-Co-66"]))
#%%
#-------------Extending the length of the anitneutrino energy list (dict3) upto 12000 keV-------------
print("88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888")
# Define the extended length
# Define the extended length
extended_length = 12000

# Create a new dictionary to store the extended sublists
print("88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888")
extended_length = 12000
# Create a new dictionary to store the extended sublists
extended_dict_3 = {}
for key1_ext in dict3:
    extended_dict_3[key1_ext] = {}
    for key2_ext in dict3[key1_ext]:
        extended_sublists = []
        if dict3[key1_ext][key2_ext]:
            extended_E_anu_sublist = max(dict3[key1_ext][key2_ext], key=len)
            for sublist in dict3[key1_ext][key2_ext]:
                longest_last_number = int(extended_E_anu_sublist[-1])
                extended_E_anu_sublist.extend(range(longest_last_number + 1, extended_length + 1))
                extended_sublists.append(extended_E_anu_sublist)
        extended_dict_3[key1_ext][key2_ext] = extended_sublists
# Now, you can check the length of the extended sublists
# print(len(extended_dict_3["Rb"]["37-Rb-98"][10]))

#%%
#--------Matching the dn_dE_normlaized dictionary. Here it should be kept in mind
#-----------that the {dn_de_normalized{key1}{key2}[[Here individual sublists are getting extended not the whole dictionary]]}
# Create a new dictionary to store the matched and extended dn_dE values
# Create a new dictionary to store the matched and extended dn_dE values
print("444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444")
matched_dn_dE_dict = {}
#print(len(dn_de_normalized_dict["Co"]["27-Co-66"]))
# Iterate through the keys in dn_de_normalized_dict
for key1_norm in dn_de_normalized_dict:
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(key1_norm)
    matched_dn_dE_dict[key1_norm] = {}    
    for key2_norm in dn_de_normalized_dict[key1_norm]:
        print("????????????????????????????????????????????????????????????????????????????????????????")
        print(key2_norm)
        extended_dn_de_sublists = []          
        for sublist in dn_de_normalized_dict[key1_norm][key2_norm]:   
            print("¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿") 
            print(len(sublist))        
            extended_sublist = None                  
            for extended_list in extended_dict_3[key1_norm][key2_norm]:
                print("ññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññññ")
                print(len(extended_list))
                if isinstance(extended_list, list) and len(sublist) < len(extended_list):
                    extended_sublist= sublist + ([0] * (len(extended_list) - len(sublist)))
                elif isinstance(extended_list, list) and len(sublist) > len(extended_list):
                    #extended_sublist= sublist + [0] * (len(extended_list) - len(sublist))
                    print("bigger than biggest number of E")
                    extended_sublist = extended_sublist
                    break 
                elif isinstance(extended_list, list) and len(extended_list) == len(sublist):
                    print("break")
                    extended_sublist = extended_sublist
                    break            
            if extended_sublist is not None:
                extended_dn_de_sublists.append(extended_sublist)
            else:
                print(f"Warning: No matching extended sublist found for {key1_norm}/{key2_norm}.")        
        matched_dn_dE_dict[key1_norm][key2_norm] = extended_dn_de_sublists
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#print(len(matched_dn_dE_dict["Co"]["27-Co-66"][0]))        

#%%
#print("28-Ni-66")
#print(len(extended_dict_3["Ni"]["28-Ni-66"][0]))
#print(matched_dn_dE_dict["Ni"]["28-Ni-66"][0])
# print("Co")
# print(extended_dict_3["Co"]["27-Co-66"][0])
# print(dn_de_normalized_dict["Co"]["27-Co-66"][0])
#Extension at the beggining 
#extended_E_anu_sublist = [0]+ extended_E_anu_sublist
for key1 in matched_dn_dE_dict:
    for key2 in matched_dn_dE_dict[key1]:
        for i in range(len(matched_dn_dE_dict[key1][key2])):
            extended_dict_3[key1][key2][i] = [extended_dict_3[key1][key2][i][0]-1] + extended_dict_3[key1][key2][i]
            matched_dn_dE_dict[key1][key2][i] = [0] + matched_dn_dE_dict[key1][key2][i]
#%%
plot_dir = "Subplots_241Pu_BetaDecay_Antineutrinospectra_xxx"
os.makedirs(plot_dir, exist_ok=True)

for key1_norm in matched_dn_dE_dict:
    print(key1_norm)
    for key2_norm in matched_dn_dE_dict[key1_norm]:
        extended_data = extended_dict_3[key1_norm][key2_norm]
        matched_data = matched_dn_dE_dict[key1_norm][key2_norm]
        
        # Assuming key1_norm and key2_norm represent element names
        endpoints = dict1.get(key1_norm, {}).get(key2_norm, [])
        
        num_sublists = len(extended_data)
        
        if len(matched_data) == 1:
            print("only one")
            plt.figure()
            plt.plot(extended_data[0], matched_data[0])
            plt.xlabel("Extended Data")
            plt.ylabel("Matched dn_dE Data")
            if endpoints:
                endpoint_str = ', '.join([f"{endpoint} KeV" for endpoint in endpoints])
                plt.title(f"Data for {key1_norm}/{key2_norm}")
                plt.suptitle(f"Endpoints: {endpoint_str}")
            else:
                plt.title(f"Data for {key1_norm}/{key2_norm}")
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plot_filename = os.path.join(plot_dir, f"{key1_norm}_{key2_norm}.png")
            plt.savefig(plot_filename)
            plt.close()
        elif len(matched_data) > 1 and len(matched_data) == len(extended_data):
            print("same length as both")
            max_subplots_per_row = 5
            num_rows = (num_sublists + max_subplots_per_row - 1) // max_subplots_per_row
            num_cols = min(num_sublists, max_subplots_per_row)            
            figsize_width = num_cols * 5
            figsize_height = num_rows * 4
            fig, axs = plt.subplots(num_rows, num_cols, figsize=(figsize_width, figsize_height), sharex=True)            
            plt.suptitle(f"Endpoint:{key1_norm}/{key2_norm}(KeV)")            
            axs_flat = axs.flatten()            
            for sublist_idx in range(num_sublists):
                ax = axs_flat[sublist_idx]
                extended_sublist = extended_data[sublist_idx]
                matched_sublist = matched_data[sublist_idx]                
                ax.plot(extended_sublist, matched_sublist)
                ax.set_xlabel("Extended Data")
                ax.set_ylabel("Matched dn_dE Data")
                if endpoints and len(endpoints) > sublist_idx:
                    ax.set_title(f"Endpoint: {endpoints[sublist_idx]} KeV")
                else:
                    ax.set_title(f"Sublist {sublist_idx + 1}")            
            for i in range(num_sublists, num_rows * num_cols):
                fig.delaxes(axs_flat[i])
            
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plot_filename = os.path.join(plot_dir, f"{key1_norm}_{key2_norm}.png")
            plt.savefig(plot_filename)
            plt.close()
        else:
            print("Different length")
print("Plots saved in the 'Subplots_241Pu_BetaDecay_Antineutrinospectra' directory.")
