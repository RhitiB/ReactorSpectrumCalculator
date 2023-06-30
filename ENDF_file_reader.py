import requests
import os
os.chdir(r"/home/rhiti/Desktop/python/95Y_corrected")
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup


output_file = 'ENDF_FILE_READER.txt'

# Iterate over the range of sect IDs
for sect_id in range(8930183, 8937857):
    url = 'https://www-nds.iaea.org/exfor/servlet/E4sGetSect?SectID={}'.format(sect_id)

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Get the content from the response
        content = response.content.decode('utf-8')

        # Write the sect ID and content to the output file
        with open(output_file, 'a') as f:
            f.write("Sect ID: {}\n".format(sect_id))
            f.write(content)
            f.write('\n---\n')  # Add a separator between each section

# Print a message indicating the process is completed
print("Values saved to '{}'".format(output_file))


