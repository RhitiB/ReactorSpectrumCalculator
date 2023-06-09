import re
import os
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

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

#print(element_names)
#%%

'''Finding the ENDF database '''

#Setting up the base URL of the system

#base_url='https://www.nndc.bnl.gov/endf/'

#Selecting the major libraries page

# Step 1: Accessing the main URL
main_url = "https://www.nndc.bnl.gov/endf/"
print(f"Accessing main URL: {main_url}")
main_response = requests.get(main_url)

if main_response.status_code == 200:
    print("Main URL accessed successfully.")
    main_soup = BeautifulSoup(main_response.content, "html.parser")

    # Step 2: Finding the library options
    library_table = main_soup.find("table", {"border": "1"})
    if library_table:
        library_options = library_table.find_all("input", {"class": "check_lib"})
        print("Library options found:")
        for option in library_options:
            library_name = option.find_next_sibling("span", {"class": "control-label"}).text.strip()
            library_status = option.get("checked")
            if library_status:
                print(f"  {library_name}: Selected")
            else:
                print(f"  {library_name}: Not Selected")

#%%

# Step 3: Selecting the ENDF library
endf_library_option = library_table.find("span", string="ENDF/B-VIII.0")
if endf_library_option:
    # Getting the input element associated with the ENDF library option
    endf_library_input = endf_library_option.find_previous("input", {"class": "check_lib"})

    # Checking if the ENDF library is already selected
    endf_library_status = endf_library_input.get("checked")
    if endf_library_status:
        endf_library_url = "https://www-nds.iaea.org/exfor/servlet/E4sSearch2"
        print(f"\nSelected library: {endf_library_url}")
        #%%

        # Step 4: Access the ENDF/B database
        # Continuing with further operations on the ENDF/B database

    else:
        # Selecting the ENDF library option
        endf_library_input["checked"] = "checked"
        endf_library_url = "https://www-nds.iaea.org/exfor/servlet/E4sSearch2"
        print(f"\nSelected library: {endf_library_url}")

else:
    print("\nENDF/B-VIII.0 option not found.")

# Navigating to the ENDF/B database URL
if endf_library_url:
    response = requests.get(endf_library_url)
    if response.status_code == 200:
        print(f"Successfully navigated to {endf_library_url}")
        # Continuing with further operations on the ENDF/B database
    else:
        print(f"Failed to navigate to {endf_library_url}")
        
#%%

# Accessing the LIST URL
if endf_library_url:
    response = requests.get(endf_library_url)
    if response.status_code == 200:
        print(f"Successfully navigated to {endf_library_url}")
        soup = BeautifulSoup(response.content, "html.parser")
        page_title = soup.find("title")
        if page_title:
            if page_title.text.strip() == "E4/Servlet: Select":
                # Proceeding to the LIST URL
                list_url = main_url + "E4sSearch2?req=12036"
                print(f"Proceeding to the LIST URL: {list_url}")

                # Continuing with further operations on the LIST URL
                # Perform the necessary actions to generate the list of evaluations

            else:
                print("Page title does not match 'E4/Servlet: Select'.")
                # Proceed with further operations on the ENDF/B database

        else:
            print("Page title not found.")
            # Proceed with further operations on the ENDF/B database

    else:
        print(f"Failed to navigate to {endf_library_url}")
        
#%%
# Accessing the LIST URL
list_url = "https://www.nndc.bnl.gov/exfor/servlet/E4sSearch2?req=12036"
print(f"Accessing the LIST URL: {list_url}")

# Accessing the LIST URL
list_response = requests.get(list_url)
if list_response.status_code == 200:
    print(f"Successfully accessed the LIST URL: {list_url}")
    list_soup = BeautifulSoup(list_response.content, "html.parser")

    # Proceed with further operations on the LIST URL
    # Perform the necessary actions to generate the list of evaluations

else:
    print(f"Failed to access the LIST URL: {list_url}")


#%%
# Setting the DECAY library URL
decay_sublib_url = "https://www-nds.iaea.org/exfor/servlet/E4sSearch2#sublibENDF/B-VIII.0_DECAY"

# Accessing the DECAY sublibrary URL
response = requests.get(decay_sublib_url)
if response.status_code == 200:
    print("Successfully accessed the DECAY sublibrary page")
    # Further processing can be done here
else:
    print("Failed to access the DECAY sublibrary page")
    
#%%
#Accessing each elements from the DECAY Library
for element in element_names:
    element_url = f"https://www-nds.iaea.org/exfor/servlet/E4sSearch2?req={element}"
    
    element_response = requests.get(element_url)
    if element_response.status_code == 200:
        print(f"Successfully accessed the data for element: {element}")
        
        # Process the data for the current element here
        
    else:
        print(f"Failed to access the data for element: {element}")

    


