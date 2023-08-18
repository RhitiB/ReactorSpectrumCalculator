import os
os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import quad
import math
import numpy as np
#%%
BR=[]
endpoints=[]
C=6.3755E-02
with open("End_BR_together.txt", "r") as file1:
    for columns in file1:
        columns=columns.split()
        endpoints.append(float(columns[0]))
        BR.append(float(columns[2]))
    #print(endpoints)
    # print(BR)
    #print(columns)
#%%
E_e_list = []
for i in range(len(endpoints)):
    if endpoints[i] < 511:
        E_e = list(range(511, int(endpoints[i])+1, -1))  # Values below 511 keV
    else:
        E_e = list(range(511, int(endpoints[i])))  # Values from 511 keV to 12000 keV
    E_e_list.append(E_e)
#print(E_e_list)
#%%

E_e_new_list = []
for sublist in E_e_list:
    new_sublist = []
    for energy in sublist:
        new_energy = energy
        new_sublist.append(new_energy)
    E_e_new_list.append(new_sublist)
#print(E_e_new_list)
#%%
E_anu_sublist=[]
for i in range(len(endpoints)):
    E_min_nu = endpoints[i] - max(E_e_new_list[i])
    E_max_nu = endpoints[i] - min(E_e_new_list[i])
    E_range = np.arange(E_min_nu, E_max_nu, 1)
    E_anu_sublist.append(E_range.tolist())  # convert keV to MeV

E_anu_list = [E_anu_sublist[i] for i in range(len(endpoints))]
#print(E_anu_list)
#to check the value of the list,
#with open("output.txt", "w") as file:
 #   for sublist in E_anu_list:
  #      file.write(str(sublist) + "\n")

#%%
def integrand(E_nu, E_o):
    expr=((E_o-E_nu)**2-1)
    if expr < 0:
        return 0
    denominator=math.sqrt(expr)* (E_nu**2)*(E_o-E_nu)
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
# print(phase_space_norm)

#%%

dn_dE_list_normalized=[]
#Multiply each element of Phase_space with the corresponding element of K
for i in range(len(endpoints)):
    P=phase_space_norm[i]
    dn_dE_2=[]
    for j in range(len(P)):
        dn_dE_2.append((C*BR[i]*P[j])/K[i]) # Multiply by the normalization constant K[i]
    dn_dE_list_normalized.append(dn_dE_2)
#print(dn_dE_list_normalized)

#%%

extended_E_anu_sublist = max(E_anu_list, key=len)
#print(longest_sublist)
extended_length = 12000
num_missing_values = extended_length - len(extended_E_anu_sublist)
#print(num_missing_values)
#extended_E_anu_sublist = longest_sublist + [0] * num_missing_values
longest_last_number= int(extended_E_anu_sublist[-1])
print(range(longest_last_number+1, extended_length))
extended_E_anu_sublist.extend(range(longest_last_number+1, extended_length))
print(extended_E_anu_sublist)
print("end of extended list")
#%%

#longest_dn_dE_sublist=max(dn_dE_list_normalized, key=len)
#print(longest_dn_dE_sublist)

matched_dn_dE = []
for sublist in dn_dE_list_normalized:
    if len(sublist) < len(extended_E_anu_sublist):
        matched_sublist = sublist + [0] * (len(extended_E_anu_sublist) - len(sublist))
        matched_dn_dE.append(matched_sublist)
    elif len(sublist) > len(extended_E_anu_sublist):
        matched_sublist = sublist[:len(extended_E_anu_sublist)]
        matched_dn_dE.append(matched_sublist)
    else:
        matched_dn_dE.append(sublist)

#print(matched_dn_dE)

#%%

def create_subplots(list_of_sublists, x_values, endpoints, save_path):
    num_subplots = len(list_of_sublists)
    num_cols = 5
    num_rows = (num_subplots + num_cols - 1) // num_cols

    # Creating the subplots
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 15), sharex=True)

    # Iterate over each sublist and create the corresponding subplot
    for i, sublist in enumerate(list_of_sublists):
        print(i)
        row_index = i // num_cols  # Calculate the row index
        col_index = i % num_cols   # Calculate the column index

        axs[row_index, col_index].plot(x_values, sublist)
        axs[row_index, col_index].set_ylabel("dn_dEnu")
        axs[row_index, col_index].set_xlabel("Antineutrino Energy (KeV)")
        axs[row_index, col_index].set_title("Endpoint {}".format(endpoints[i]))
        axs[row_index, col_index].set_ylim(0, max(sublist) * 1.2)
        # Uncomment the following lines if you want to set custom x-axis limits
        # axs[row_index, col_index].set_xlim(min(x_values), max(x_values))
        # if i == num_subplots - 1:
        #     axs[row_index, col_index].set_xlim(min(x_values), max(x_values) * 0.8)

    plt.tight_layout()  # Adjust the spacing between subplots

    # Save the plot before showing it
    plt.savefig(save_path)
    plt.show()

list_of_sublists = matched_dn_dE
x_values = extended_E_anu_sublist  # Use the correct x-values here
endpoints = range(len(matched_dn_dE))  # Assuming endpoints are numbered from 1 to the number of subplots
save_path = 'Subplots_of_Y95_new.png'
create_subplots(list_of_sublists, x_values, endpoints, save_path)
#print(len(x_values))
#print(list_of_sublists[19])
