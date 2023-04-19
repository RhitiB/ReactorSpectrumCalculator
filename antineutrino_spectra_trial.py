import os
import random
os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import quad
import math
endpoints=[]
BR=[]
K=[]
C=6.3755E-02 #Cumulative Yield (for our requirements, we are considering the thermal range)

with open("End_BR_together.txt") as file1:
    for columns in file1:
        columns=columns.split()
        #print(columns)
        endpoints.append(float(columns[0]))
        BR.append(float(columns[2]))
    #print(endpoints)
    #print(BR)

with open("E_nu_values.txt", "w") as file:
    for i in range(len(endpoints)):
        if endpoints[i] < 511:
            E_e = list(range(511, int(endpoints[i])+1, -1))
            E_nu = [endpoints[i] - E for E in E_e]
        else:
            E_e = list(range(511, int(endpoints[i])))
            E_nu = [endpoints[i] - E for E in E_e]
        
        # Write E_nu values to file
        for value in E_nu:
            file.write(str(value) + "\n")
            print(value)
E_nu_list=[]            
with open("E_nu_values.txt", "r") as file2:
    for columns in file2:
        columns=columns.split()
        print(columns)
        E_nu_list.append(float(columns[0]))
    print(E_nu_list)
    
'''Phase space calculation'''


    
        
    
        


        
        

    
    
        
    

    

