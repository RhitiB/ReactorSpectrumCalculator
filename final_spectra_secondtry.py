import os
os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
import math
import matplotlib.pyplot as plt


endpoints=[]
BR=[]
with open("End_BR_together.txt", "r") as file1:
    for columns in file1:
        columns=columns.split()
        #print(columns)
        endpoints.append(float(columns[0]))
        BR.append(float(columns[2]))
    print(endpoints) #endpoints are in KeV units
    print()
    #print(BR)
    
'''Electron momentum calculation'''
E_e=511 #KeV
p_e=math.sqrt((E_e)**2-1)
print(p_e)

print()

'''Normalization constant'''
K_norm=[]
for columns in range(len(endpoints)):
    K=12/(p_e*(endpoints[columns])**4)
    print(K)
    K_norm.append(float(K))
print()
print(K_norm)
print()
#Phase space calculation
Phase_space_list=[]
for data in range(len(K_norm)):
    Phase_space=(K_norm[data]*p_e*E_e*(endpoints[data]-E_e)**2)
    print(Phase_space)
    Phase_space_list.append(float(Phase_space))
print(Phase_space_list)

#dn_dE value
cum_yield=6.3755E-02
dn_dE_list=[]
for data in range(len(Phase_space_list)):
    dn_dE=cum_yield*BR[data]*Phase_space_list[data]
    print(dn_dE)
    dn_dE_list.append(float(dn_dE))
print()
print(dn_dE_list)

#FINAL SPECTRA    
Q_value_eV = 4.4500E+06
Q_value_keV = Q_value_eV * 0.001
print(Q_value_keV)

# Calculate energy bin size
num_endpoints = len(endpoints)
bin_size = Q_value_keV / num_endpoints
print(bin_size)


#Calculate the Kinetic energy
num_endpoints=20
bin_size=222.5
kinetic_energies = [(i+1)*bin_size for i in range(num_endpoints)]
print(kinetic_energies)

# Calculate total number of electrons
total_counts = 0
for i in range(len(dn_dE_list)):
    total_counts += dn_dE_list[i]   # Sum the dN/dE values for all energy bins
total_counts *= bin_size
print(total_counts)

#Calculate the normalied dn_dE values. 
normalized_dN_dE = []
for i in range(len(dn_dE_list)):
    normalized = dn_dE_list[i] / (total_counts * bin_size)   # Divide by total number of counts
    normalized_dN_dE.append(normalized)
print(normalized_dN_dE)

plt.plot(kinetic_energies, dn_dE_list)

plt.show()
    
    



