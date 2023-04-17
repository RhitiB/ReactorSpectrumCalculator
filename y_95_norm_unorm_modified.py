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

'''FIRST:UN-NORMALIZED PART'''

'''1. Calculation of the unnormalized phase space'''

Phase_space=[]
for i in range(len(endpoints)):
    if endpoints[i]<511:
        E_e = list(range(511, int(endpoints[i])+1, -1))
    else:
        E_e=range(511, int(endpoints[i]))
    
    #print(E_e)
    endpoint_phase_space = []

    # Calculate the phase space for each electron energy
    for j in range(len(E_e)):
        P = math.sqrt(E_e[j]**2-1) * E_e[j] * (endpoints[i]-E_e[j])**2
        #Appending values of each endpoints to each phase space list
        endpoint_phase_space.append(P)

    # Append the phase space list for this endpoint to the overall list
    Phase_space.append(endpoint_phase_space)
    
#for i in range(len(Phase_space)):
    #print("Endpoint {}: {}\n".format(endpoints[i], Phase_space[i]))
    
'''2. Calculation of unnormalized dn_dE'''
dn_dE_list=[]
for i in range(len(endpoints)):
    P=Phase_space[i]
    dn_dE_1=[]
    for j in range(len(P)):
        dn_dE_1.append(C*BR[i]*P[j])
    #print(dn_dE)
    dn_dE_list.append(dn_dE_1)
#print(dn_dE_list)

'''SECOND:NORMALIZATION'''

'''1.Calculation of the Integral'''

# Calculation of normalization constant for a single endpoint energy. The normalization
#is done by taking into consideration of one endpoint value by comparing it with the rest

endpoint = 4449.78  # KeV (this value can change according to our desired endpoint energy)

def integrand(E_e, E_o):
    denominator = ((E_e**2 - 1)**0.5 * E_e * (E_o - E_e)**2)
    if denominator.imag != 0:
        return 0
    else:
        return 1 / denominator.real

E_min = 511  # KeV, minimum electron energy

normalization_K = quad(integrand, E_min, endpoint, args=(endpoint,))[0]
#print(normalization_K)
#print("Normalization constant (K) = {}".format(normalization_K))

#Normalization constant for endpoint energy 4449.78: [3.145925282926117e-10]
'''2. Normalized phase space calculation'''

Phase_space_norm=[]
for i in range(len(endpoints)):
    if endpoints[i]<511:
        E_e = list(range(511, int(endpoints[i])+1, -1))
    else:
        E_e=range(511, int(endpoints[i]))
    endpoint_phase_space = []
    # Calculate the phase space for each electron energy
    # Calculate the phase space for each electron energy
    for j in range(len(E_e)):
        P = normalization_K*math.sqrt(E_e[j]**2-1) * E_e[j] * (endpoints[i]-E_e[j])**2
        #Appending values of each endpoints to each phase space list
        endpoint_phase_space.append(P)
    Phase_space_norm.append(endpoint_phase_space)
#for i in range(len(Phase_space_norm)):
    #print("Endpoint {}: {}\n".format(endpoints[i], Phase_space_norm[i]))
    
    
dn_dE_list_normalized=[]
#Multiply each element of Phase_space with the corresponding element of K
for i in range(len(endpoints)):
    P=Phase_space_norm[i]
    dn_dE_2=[]
    for j in range(len(P)):
        dn_dE_2.append(C*BR[i]*P[j]) 
    dn_dE_list_normalized.append(dn_dE_2)
#print(dn_dE_list_normalized)

#set up the subplots
num_plots = len(endpoints)
num_cols=5
num_rows = int(num_plots / num_cols) + int(num_plots % num_cols > 0)

#Creating a file for writing the data

with open("Output_data_Y-95.txt", "w") as output:
    
    for i in range(num_plots):
        
        if endpoints[i]<511:
            E_e = list(range(511, int(endpoints[i])+1, -1))
        else:
            E_e=range(511, int(endpoints[i]))
    
       #Get the dn_dE values for the un-normalized case
        dn_dE_unnorm= dn_dE_list[i]
    
       # Get the dn_dE values for the normalized case
        dn_dE_norm = dn_dE_list_normalized[i]
        # Print the data to the file
        #output.write("Endpoint {}\n".format(endpoints[i]))
        #output.write("E_e (keV)     dn_dE      dn_dE normalized\n")
        for j in range(len(E_e)):
           output.write("{}   {}    {}\n".format(E_e[j], dn_dE_unnorm[j], dn_dE_norm[j]))
        output.write("\n")
#Create the subplots

fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))
    
       #Plotting of the graphs
for i in range(num_plots):
    #Get the electron energies for the current endpoint
    if endpoints[i]<511:
        E_e = list(range(511, int(endpoints[i])+1, -1))
    else:
        E_e=range(511, int(endpoints[i]))

    #Get the dn_dE values for the un-normalized case
    dn_dE_unnorm= dn_dE_list[i]

    # Get the dn_dE values for the normalized case
    dn_dE_norm = dn_dE_list_normalized[i]

    #Get the row and column index for the current subplot
    row_index = int(i / num_cols)
    col_index = i % num_cols

    # Plotting the graph without normalization constant for the current endpoint
    axes[row_index, col_index].plot(E_e, dn_dE_unnorm, color="blue")
    axes[row_index, col_index].set_xlim([511, int(endpoints[i])])
    axes[row_index, col_index].set_xlabel('Electron energy (keV)')
    axes[row_index, col_index].set_ylabel('dn_dE')
    axes[row_index, col_index].set_title('Endpoint {}'.format(endpoints[i]))

    #Plotting the graph with the normalization for thr current endpoint
    axes[row_index, col_index].plot(E_e, dn_dE_norm, color="red")
    axes[row_index, col_index].legend(['unnormalized', 'normalized'])

# Show the subplots
plt.tight_layout()
plt.savefig("Individual_spectra_y95.pdf")
plt.show()






