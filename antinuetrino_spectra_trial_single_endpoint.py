import os
os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import quad
import math
BR=3.54 
endpoint=1200.79
C=6.3755E-02

    
E_e_list=[]
E_e = list(range(511, int(endpoint)))
#print(E_e)
E_e_list.append(E_e)
#print(E_e_list)

for i in range(len(E_e_list)):
    E_anu_min = endpoint - min(E_e_list[i])
    E_anu_max = endpoint - max(E_e_list[i])
    E_anu = []
    for energy in range(int(E_anu_max), int(E_anu_min)  +1):
        E_anu.append(energy)
    #print(E_anu)
    
p_nu_list=[]
for i in range(len(E_anu)):
    P=math.sqrt((endpoint - E_anu[i])**2 - 1) * E_anu[i]**2 * (endpoint - E_anu[i])
    #print(P)
    p_nu_list.append(P)
#print(p_nu_list)

dn_dEanu=[]
for i in range(len(p_nu_list)):
    dn_dE_anu=C*BR*p_nu_list[i]
    #print(dn_dE_anu)
    dn_dEanu.append(dn_dE_anu)
print(dn_dEanu)

plt.plot(E_anu, dn_dEanu)
plt.show()
    





