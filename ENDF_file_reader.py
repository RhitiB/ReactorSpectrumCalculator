import re
import os
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

#%%
'''element_names = []
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

print(element_names)'''
#%%
import requests

output_file = 'ENDF_FILE_READER.txt'

# Iterate over the range of sect IDs
for sect_id in range(8930183, 8937858):
    url = 'https://www-nds.iaea.org/exfor/servlet/E4sGetSect?SectID={}'.format(sect_id)

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Get the content from the response
        content = response.content.decode('utf-8')

        # Write the sect ID and content to the output file
        with open(output_file, 'a') as f:
            f.write(f"Sect ID: {sect_id}\n")
            f.write(content)
            f.write('\n---\n')  # Add a separator between each section

# Print a message indicating the process is completed
print("Values saved to '{}'".format(output_file))

#%%

'''This program only reads the ENDF file with the section-ID. The output file name can be changed 
as per convinience'''