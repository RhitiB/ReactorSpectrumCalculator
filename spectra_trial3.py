#%%

import os
os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import quad
import math
import numpy as np
BR=[]
endpoints=[]
C=6.3755E-02
with open("End_BR_together.txt", "r") as file1:
    for columns in file1:
        columns=columns.split()
        endpoints.append(float(columns[0])) #in MeV
        BR.append(float(columns[2]))
    #print(endpoints)
    # print(BR)
    #print(columns)
#%%
E_e_list=[]

for i in range(len(endpoints)):
    if endpoints[i]<511:
        E_e = list(range(511, int(endpoints[i])+1, -1))
    else:
        E_e=list(range(511, int(endpoints[i])))
        #print(E_e)
    E_e_list.append(E_e)
#print(E_e_list)

E_e_new_list = []
for sublist in E_e_list:
    new_sublist = []
    for energy in sublist:
        new_energy = energy  # convert keV to MeV
        new_sublist.append(new_energy)
    E_e_new_list.append(new_sublist)
#print(E_e_new_list)
#%%

E_anu_list=[]
for i in range(len(endpoints)):
    E_min_nu=endpoints[i] - max(E_e_new_list[i])
    #print(E_min_nu)
    E_max_nu = endpoints[i] - min(E_e_new_list[i])
    # print(E_max_nu)
    E_range = np.arange(E_min_nu, E_max_nu, 0.01)
    E_anu_list.append(E_range.tolist()) #convert keV to MeV
#print(E_anu_list)
print(len(E_anu_list))

#%%
def integrand(E_nu, E_o):
    expr=((E_o-E_nu)**2-1)
    if expr < 0:
        return 0
    denominator=math.sqrt(expr)* E_nu**2*(E_o-E_nu)
    if denominator.imag != 0:
        return 0
    else:
        return 1/denominator.real

K=[]
E_nu_min=1.8 #MeV
for i in range(len(endpoints)):
    normalization=quad(integrand, E_nu_min, endpoints[i], args=(endpoints[i],))[0]
    K.append(normalization)
#print(K)

#%%
phase_space_norm = []
#print(len(endpoints), len(E_anu_list))
for i in range(len(endpoints)):
    phase_space = []
    for j in range(len(E_anu_list[i])):
        expr = (endpoints[i] - E_anu_list[i][j])**2 - 1
        if expr < 0:
            continue
        P = math.sqrt(expr) * E_anu_list[i][j]**2 * (endpoints[i] - E_anu_list[i][j])
        if endpoints[i] <= 0:
            continue
        phase_space.append(P)
    phase_space_norm.append(phase_space)
#print(phase_space_norm)

#%%
dn_dE_list_normalized=[]
#Multiply each element of Phase_space with the corresponding element of K
for i in range(len(endpoints)):
    P=phase_space_norm[i]
    dn_dE_2=[]
    for j in range(len(P)):
        dn_dE_2.append(C*BR[i]*K[i]*P[j]) # Multiply by the normalization constant K[i]
    dn_dE_list_normalized.append(dn_dE_2)
#print(dn_dE_list_normalized)
#print(len(dn_dE_list_normalized))
#%%
#set up the subplots
'''num_plots = len(endpoints)
num_cols=5
num_rows = int(num_plots / num_cols) + int(num_plots % num_cols > 0)
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))

#Plotting of the graphs

for i in range(num_plots):
    #Get the electron energies for the current endpoint
    E_e = range(511, int(endpoints[i]))
    
    #Get the dn_dE values for the un-normalized case
    dn_dE_norm= dn_dE_list_normalized[i]
    
    #Get the row and column index for the current subplot
    row_index = int(i / num_cols)
    col_index = i % num_cols
    
    # Plotting the graph without normalization constant for the current endpoint
    
    axes[row_index, col_index].set_xlabel('Antineutrino energy (KeV)')
    axes[row_index, col_index].set_ylabel('dn_dE')
    axes[row_index, col_index].set_title('Endpoint {}'.format(endpoints[i]))
    
    #Plotting the graph with the normalization for thr current endpoint
    axes[row_index, col_index].plot(E_anu_list[i], dn_dE_norm, color="red")
    axes[row_index, col_index].legend(["normalized"])
    
    # Show the subplots
plt.tight_layout()
plt.savefig("Individual_spectra_y95.pdf")
plt.show()'''