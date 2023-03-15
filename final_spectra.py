import os
os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
import math
import matplotlib.pyplot as plt

from scipy.integrate import quad
endpoints=[]
BR=[]
with open("End_BR_together.txt", "r") as file1:
    for columns in file1:
        columns=columns.split()
        #print(columns)
        endpoints.append(float(columns[0]))
        BR.append(float(columns[2]))
    #print(endpoints)
    print()
    #print(BR)
    
'''Normalization constant calculation'''

E_e=511 #KeV    
m_e = 9.109e-31 # kg (electron rest mass)
c = 299792458 # m/s (speed of light)
P_e=math.sqrt(E_e**2 - (m_e*c**2)**2) # in keV/c
#print("The momentum of the electron is {:.3f} keV/c".format(P_e))
'''Integral'''
integral=[]
def integrand(E_e, E0):
    return E_e * (E0 - E_e)**2
E0_list = endpoints
for E0 in E0_list:
    result, _ = quad(integrand, 0, E0, args=(E0,))
    #print(f"Result for E0={E0}: {result}")
    integral.append(float(result))
integrand(E_e, E0) 
#print(integral)
K_norm=[]
for i in range(len(integral)):
    K=1/(P_e*integral[i])
    #print(K)
    K_norm.append(float(K))
#print(K_norm)

'''Phase space calculation'''
Phase_space_list=[]
for data in range(len(K_norm)):
    Phase_space=(K_norm[data]*P_e*E_e*(endpoints[data]-E_e)**2)
    #print(Phase_space)
    Phase_space_list.append(float(Phase_space))
#print(Phase_space_list)
    
'''dn_dE value'''
cum_yield=6.3755E-02
dn_dE_list=[]
for data in range(len(Phase_space_list)):
    dn_dE=cum_yield*BR[data]*Phase_space_list[data]
    #print(dn_dE)
    dn_dE_list.append(float(dn_dE))
print(dn_dE_list)
print()
print()


'''FINAL SPECTRA'''    
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

plt.plot(kinetic_energies, normalized_dN_dE)
plt.show()



    




    
   


    
    
   
        
        
