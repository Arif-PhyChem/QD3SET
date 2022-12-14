from dataset import qddset 

# From qd3set module we import qddset class.

# parameter details

# extr_choice: str
# methodType: str
# FMOtype:  str
# dataPath: str
# Nsites: int

#***********************
#   Detail 
#***********************

# extr_choice (extraction choice):
# We can pass multiple extraction choices. For instance, To extract data with site-1 as initial excitation, 
# pass extr_choice = 'site-1'. For extraction of site-6 data, 
# pass extr_choice = 'site-6' and similarly for site-8 data pass 'site-8'. 
# To extract all data, just pass 
# extr_choice = 'all'. The default choice is 'cal_details' which 
# only shows calculation details.   
# For spin-boson model, extr_choices are 'all', 'sym', 'asym', and 'cal_details'.

# systemType (system type): 
# Pass 'SB' for spin-boson and 'FMO' for FMO complex

# methodType (method type):
# Pass 'HEOM' or 'LTLME' for the extraction of the corresponding data

# FMOtype: (Type of FMO):
# In our dataset, we have generated LTLME data with two Hamiltonians for both 
# 7-site and 8-site FMO. Here we represent them as I and II. check output.details
# for more

# dataPath (path to data directory)

# Nsites (number of sites in FMO case)
# it can be 7, 8, or 24 (for trimer)

param = {'extr_choice': 'asym',
        'systemType': 'SB',
        'methodType': 'HEOM', 
        'FMOtype' : 'II', # matters only in LTLME case for 7-sites and 8-sites FMO
        'dataPath': 'heom_sb/data',
        'Nsites': 8,  # only wanted for FMO 
        }
qddset = qddset(**param) #  initializing parameters
output = qddset.extract() # extracting the data

#***********************
#  Output details
#***********************

# If the extr_choice : cal_details, then we only get calculation details and Hamiltonian

# print(output.details and output.H)

# If extr_choice is some other choice, then we get the following data
#  output.details for calculation details
#  output.H for Hamiltonian
#  output.N_trajs to see the number of trajectories
# output.gamma to see the values of gamma (cutoff frequencies of bath)
# output.lamb to see the values of lambda (system bath coupling strengths)
# output.temp to see the values of temperature
# output.epsilon to see the values of energy difference in the case of spin-boson model
# output.Delta  to see the values of coupling strength between the two states in spin-boson model
# data = list(output.data.values()) makes the trajectories accessible. With data[i], we
# access the ith trajectory

print(output.details, output.H, output.epsilon, output.Delta, output.N_trajs, output.gamma, output.lamb, output.beta)
data = list(output.data.values())
print(data[0])
