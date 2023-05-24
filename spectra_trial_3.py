
import os
#os.chdir(r"C:\Users\basur\OneDrive\Desktop\python\95Y_corrected")
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
print(phase_space_norm)


#with open("output.txt", "w") as file:
 #   for sublist in phase_space_norm:
  #      file.write(str(sublist) + "\n")



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

#with open('output.txt', 'w') as file:
 #   for sublist in dn_dE_list_normalized:
  #      file.write(str(sublist)+ '\n')


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
#%%
#Finding the maximum length of the lists: The calculation is done by finding the minimum length of each sublist
#in both the E_anu_list and in the dn_dE_normalized_list
def maximum_length(lst):
    max_length = 0

    for sublist in lst:
        length = len(sublist)
        if length > max_length:
            max_length = length

    return max_length
max_length_dn_dE = maximum_length(dn_dE_list_normalized)
print("Maximum dn_dE_sublist length:", max_length_dn_dE)

#%%
#This is used to match the length of the sublists with zeros for adjusting the length of the arrays.
def match_sublist_lengths(lst):
    max_length = maximum_length(lst)
    for sublist in lst:
        while len(sublist) < max_length:
            sublist.append(0)
    return(lst)
matched_dn_dE = match_sublist_lengths(dn_dE_list_normalized)
print((matched_dn_dE))
#with open('output.txt', 'w') as file:
 #   for sublist in matched_dn_dE:
  #      file.write(str(sublist)+ '\n')
#for i, sublist in enumerate(matched_dn_dE):
    #length = len(sublist)
    #print("Length of sublist", i, ":", length)
#for i in matched_dn_dE:
    #print(matched_dn_dE[7])

#%%
#This is done seperately to find the longest sublist in the E_anu_list which can cover the maximum range of the
#antineutrino spectra. This sublist is used for plotting the spectra for all the subplots with their respective endpoints.

def longest_sublist_with_max_value(lst):
    max_value = float('-inf')  # Initializing max_value as negative infinity
    longest_sublist = []
    for sublist in lst:
        sublist_max = max(sublist)  # Find the maximum value in the sublist
        if sublist_max > max_value:
            max_value = sublist_max
            longest_sublist = sublist
        elif sublist_max == max_value and len(sublist) > len(longest_sublist):
            longest_sublist = sublist
    return longest_sublist
my_list = E_anu_list
longest_sublist = longest_sublist_with_max_value(my_list)
#print("Longest sublist with maximum value:", longest_sublist)

#%%
def create_subplots(list_of_sublists, x_values, endpoints,save_path):
    num_subplots = len(list_of_sublists)
    num_cols = 5
    num_rows = (num_subplots + num_cols - 1) // num_cols

    # Creating the subplots
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 15), sharex=True)

    # Iterate over each sublist and create the corresponding subplot
    for i, sublist in enumerate(list_of_sublists):
        row_index = i // num_cols  # Calculate the row index
        col_index = i % num_cols   # Calculate the column index

        axs[row_index, col_index].plot(x_values, sublist)
        axs[row_index, col_index].set_ylabel("dn_dEnu")
        axs[row_index, col_index].set_xlabel("Antineutrino Energy (KeV)")
        axs[row_index, col_index].set_title("Endpoint {}".format(endpoints[i]))

    plt.tight_layout()  # Adjust the spacing between subplots
    plt.show()
    plt.savefig(save_path)

list_of_sublists = matched_dn_dE
x_values = longest_sublist
save_path=('Subplots of Y95.png')
create_subplots(list_of_sublists, x_values, endpoints, save_path)

#%%

####Weighted_Sum'########










































