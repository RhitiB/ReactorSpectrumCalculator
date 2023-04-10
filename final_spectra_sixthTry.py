import os
import random
os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math
#First endpoint
C=6.3755E-02 #Cumulative Yield
endpoints=[]
BR=[]
dn_dE_list=[]
with open("End_BR_together.txt") as file1:
    for columns in file1:
        columns=columns.split()
        #print(columns)
        endpoints.append(float(columns[0]))
        BR.append(float(columns[2]))
    #print(endpoints)
    #print(BR)
    
'''PHASE SPACE'''

Phase_space=[]
for i in range(len(endpoints)):
    E_e=range(511, int(endpoints[i]))
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
    

for i in range(len(endpoints)):
    P=Phase_space[i]
    dn_dE=[]
    for j in range(len(P)):
        dn_dE.append(C*BR[i]*P[j])
    #print(dn_dE)
    dn_dE_list.append(dn_dE)
print(dn_dE_list)


# Set up the subplots
num_plots = len(endpoints)
num_cols = 5
num_rows = int(num_plots / num_cols) + int(num_plots % num_cols > 0)
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))

# Plot the graphs
for i in range(num_plots):
    # Get the electron energies for the current endpoint
    E_e = range(511, int(endpoints[i]))

    # Get the dn_dE values for the current endpoint
    dn_dE = dn_dE_list[i]
    #print(dn_dE)

    # Get the row and column index for the current subplot
    row_index = int(i / num_cols)
    col_index = i % num_cols

    # Plot the graph for the current endpoint
    axes[row_index, col_index].plot(E_e, dn_dE)
    axes[row_index, col_index].set_xlim([511, int(endpoints[i])])
    #axes[row_index, col_index].set_yscale("log")
    axes[row_index, col_index].set_xlabel('Electron energy (keV)')
    axes[row_index, col_index].set_ylabel('dn_dE')
    axes[row_index, col_index].set_title('Endpoint {}'.format(endpoints[i]))

# Show the subplots
plt.tight_layout()
plt.show()
plt.savefig("Beta_Spectra_95_Y.pdf")






