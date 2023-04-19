#import openmc
import os
os.chdir("/home/rhiti/Desktop/bash_scripts")
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

E_e_list=[]
for i in range(len(endpoints)):
    if endpoints[i] < 511:
        E_e = list(range(511, int(endpoints[i])+1, -1))
    else:
        E_e = list(range(511, int(endpoints[i])))
    #print(E_e)
    E_e_list.append(E_e)

#print(E_e_list)
E_anti_nu_list=[]
for i in range(len(endpoints)):
    E_min_nu = endpoints[i] - max(E_e_list[i])
    E_max_nu = endpoints[i] - min(E_e_list[i])
    #print("Endpoint:", endpoints[i])
    #print([E_min_nu, E_max_nu]) 
    E_range = list(range(int(E_min_nu), int(E_max_nu)+1))
    E_anti_nu_list.append(E_range)
#print(E_anti_nu_list)

phase_space_list=[]
for i in range(len(endpoints)):
    #if i < len(E_anti_nu_list):
        for j in range(len(E_anti_nu_list[i])):
            P = math.sqrt((endpoints[i] - E_anti_nu_list[i][j])**2 - 1) * E_anti_nu_list[i][j]**2 * (endpoints[i] - E_anti_nu_list[i][j])
            #print(P)
            phase_space_list.append(P)
print(phase_space_list)


        
    
    
   



   












