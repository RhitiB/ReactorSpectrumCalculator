import os
os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import quad
import math
BR=[]
endpoints=[]
C=6.3755E-02
with open("End_BR_together.txt", "r") as file1:
    for columns in file1:
        columns=columns.split()
        endpoints.append(float(columns[0]))
        BR.append(float(columns[2]))
    #print(endpoints)
    #print(BR)
        #print(columns)
E_e_list=[]
for i in range(len(endpoints)):
    if endpoints[i] < 511:
        E_e = list(range(511, int(endpoints[i])+1, -1))
    else:
        E_e = list(range(511, int(endpoints[i])))
    #print(E_e)
    E_e_list.append(E_e)

#print(E_e_list)
E_anu_list=[]
for i in range(len(endpoints)):
    E_min_nu = endpoints[i] - max(E_e_list[i])
    E_max_nu = endpoints[i] - min(E_e_list[i])
    #print("Endpoint:", endpoints[i])
    #print([E_min_nu, E_max_nu]) 
    E_range = list(range(int(E_min_nu), int(E_max_nu)+1))
    E_anu_list.append(E_range)
#print(E_anu_list)

P_list = []

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
    P_list.append(phase_space)
    
#print(P_list)
#for i, sublist in enumerate(P_list):
    #print(f"Phase space for endpoint {endpoints[i]}: {sublist}\n")
            
dn_dEnu_list=[]
for i in range(len(endpoints)):
    P=P_list[i]
    dn_dEnu=[]
    for j in range(len(P)):
        dn_dEnu.append(C*BR[i]*P[j])
    #print(dn_dE)
    dn_dEnu_list.append(dn_dEnu)
#print(dn_dEnu_list)

#for i, sublist in enumerate(dn_dEnu_list):
    #print(f"dN_dE_nu for endpoint {endpoints[i]}: {sublist}\n")
    
#To create the subplots
num_plots = len(endpoints)
num_cols=5
num_rows = int(num_plots / num_cols) + int(num_plots % num_cols > 0)
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))
for i in range(num_plots):
    
        
    dn_dE_anu= dn_dEnu_list[i]
    #Get the row and column index for the current subplot
    row_index = int(i / num_cols)
    col_index = i % num_cols
    # Plotting the graph without normalization constant for the current endpoint
    axes[row_index, col_index].plot(E_anu_list[i], dn_dE_anu, color="magenta")
    #axes[row_index, col_index].set_xlim([511, int(endpoints[i])])
    axes[row_index, col_index].set_xlabel(r"$E_{\nu}$ (MeV)")
    axes[row_index, col_index].set_ylabel(r"$\frac{dN}{dE_{\nu}}$")
    axes[row_index, col_index].set_title('Endpoint {}'.format(endpoints[i]))
    #axes[row_index, col_index].legend()
    
plt.tight_layout()
plt.savefig("Antineutrino_spectra_Y95.png")
plt.show()

            



    

    
    
        
        
        
        
