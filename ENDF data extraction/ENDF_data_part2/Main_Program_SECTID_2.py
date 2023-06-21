import os
import re
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time
import webbrowser
#%%

base_url = "https://www-nds.iaea.org/exfor/servlet/E4sGetSect?SectID="
output_file = "ENDF_data_2.txt"

last_sectID_2 = 8937209
current_sectID_2 =8937159

with open(output_file, "w") as file:
    while current_sectID_2 <= last_sectID_2:
        url = base_url + str(current_sectID_2)
        response = requests.get(url)
    
        # Write the sectID and response content to the file
        file.write(f"sectID: {current_sectID_2}\n")
        file.write(response.text)
        file.write("\n\n")
    
        current_sectID_2 += 2