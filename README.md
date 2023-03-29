# QD3SET-1: A Database with Quantum Dissipative Dynamics Data sets
**This package is provided to make easy the extraction of data from our QD3SET-1 databasse. Our QD3SET-1 database 8 datasets with trajectories propagated for reduced density matrix of spin-boson model and FMO complex. Two methods were used: Local-thermalizing Lindblad Equation of Motion (LTLME) and Hierarachical Equations of Motion (HEOM). For more details, please read our article " Arif Ullah, Luis E. Herrera Rodriguez, Pavlo O. Dral, and Alexei A. Kananenka, QD3SET-1: A Database with Quantum Dissipative Dynamics Data sets https://doi.org/10.48550/arXiv.2301.12096**

**In ```example.ipynb```, we demonstrate how to use this package for extraction of data**

To use the package, we need to import ```qddset``` class from ```dataset.py``` module

```from dataset import qddset```

### Parameters to pass are
 ```
 extr_choice: dtpe =  str 
 methodType: dtype = str  
 FMOtype:  dtype = str  
 dataPath:  dtype =  str  
 Nsites: dtype =  int  
```
***********************
##   Details 
***********************

### ```extr_choice``` (extraction choice):
 We can pass multiple extraction choices. For instance, To extract data with site-1 as initial excitation, 
 pass ```extr_choice = 'site-1'```. For extraction of site-6 data, 
 pass ```extr_choice = 'site-6'``` and similarly for site-8 data pass ```'site-8'```. 
 To extract all data, just pass ```extr_choice = 'all'```. The default choice is ```'cal_details'``` which 
 only shows calculation details. For spin-boson model, extr_choices are ```'all'```, ```'sym'```, ```'asym'```, and ```'cal_details'```.

### ```systemType``` (system type): 
Pass ```'SB'``` for spin-boson and ```'FMO'``` for FMO complex

### ```methodType``` (method type):
Pass ```'HEOM'``` or ```'LTLME'``` for the extraction of the corresponding data

### ```FMOtype``` (Type of FMO):
 In our dataset, we have generated LTLME data with two Hamiltonians for both 
 7-site and 8-site FMO. Here we represent them as ```I``` and ```II```. check ```output.details```
 for more

### ```dataPath``` (path to data directory):

### ```Nsites``` (number of sites in FMO case):
 it can be 7, 8, or 24 (for trimer)

### Defining input parameters 
```
param = {'extr_choice': 'site-1', 
        'systemType': 'FMO', 
        'methodType': 'HEOM',
        'FMOtype' : 'II',
        'dataPath': 'HEOM_data',
        'Nsites': 8, 
        }
 ```       
   
### Pass the param
```
dataset = qddset(**param) #  initializing parameters \
output = dataset.extract() # extracting the data
```
***********************
###  Output details
***********************

 If the ```extr_choice : cal_details```, then we only get calculation details and Hamiltonian 
``` print(output.details and output.H)```

 If extr_choice is some other choice, then we get the following data:
 
 ```output.details``` for calculation details
 
 ```output.H``` for Hamiltonian
 
 ```output.N_trajs``` to see the number of trajectories
 
 ```outout.initial_site``` to see the site with initial excitation (only in FMO complex) 
 
 ```output.gamma``` to see the values of gamma (cutoff frequencies of bath in units of cm-1)
 
 ```output.lamb``` to see the values of lambda (system bath coupling strengths in units of cm-1)
 
 ```output.temp``` to see the values of temperature in units of K (in the case of FMO)
 
  ```output.beta``` to see the values of inverse temperature in units of (a.u.) (in the case of spin-boson model)
 
 ```output.epsilon``` to see the values of energy difference in the case of spin-boson model
 
 ```output.Delta```  to see the values of coupling strength between the two states in spin-boson model
 
 ```data = list(output.data.values())``` makes the trajectories accessible. With ```data[i]```, we
 access the ith trajectory

### To print the output 

```print(output.details, output.H, output.N_trajs, output.gamma, output.lamb, output.temp, output.beta, output.epsilon, output.Delta)```

```data = list(output.data.values())```

```print(data[0])```  print the 1st trajectory
