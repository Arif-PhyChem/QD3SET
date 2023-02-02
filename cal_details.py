#%%%%%%%%%%%%%%---Spin-boson model---%%%%%%%%%%%%
def heom_sb_details():
    details=" \n ****************************************************************\n  In the spin-boson calculations, \
we consider both symmetric and asymmetric cases and for each case, we generate 500 trajectories. \
The data is generated with the HEOM method implemented in the QuTip package (v.2.6)  [https://qutip.org/]. \
The hierarchy depth \'L\' was set 30 and the number of Mastsubara terms \'K\'  was changed with temperature, i,e., \
beta = 0.1 K = 2, beta = 0.25 K = 3, beta = 0.5 K = 3, beta = 0.75 K = 4, beta = 1.0 K = 5. The time-step for \
propagation was set to dt = 0.05 and values were recorded for each dt = 0.1. \
In spin-boson model, the Hamiltonian is written as \n H = [epsilon,  Delta \n     Delta*,  0] \n. For symmetric case, epsilon is 0 and we set it to 1 for asymmetric case. For both cases, Delta is 1. \n From the database, the data \
and the corresponding parameters can be extracted as;  You can pass \
an extraction choice with keyword \"function(extr_choice: choice)\". \
The choice here is \'all\', \'sym\', \'asym\' or \'cal_details\' \
which extracts data for the corresponding choice. The default choice is the 'cal_details' which \
provides details about the calculations. \n \n  From the output of the function, you can access the data \
as: \'output.data\' (for trajectories), \'output.N_trajs\' (total number of trajectories), \
\'output.epsilon\' (energy difference between the two states), \'output.Delta\' (interaction strength between the two states)  \
,\'output.gamma\' (the cutoff frequencies for all trajectories), \'output.lamb\' (the system-bath \
coupling strengths for all trajectories) and the \'output.beta\' (inverse temperature values for all trajectories).\
\n \n  It is worth-emphasizing that \'output.data\' is a dictionary and to extract the data, you can use \
\'xyz=list(output.data.values())\', where \'xyz[i]\' gives you the ith trajectory \
corresponding to the ith value in the epsilon, Delta, gamma ,lamb and  temp (all parameters are in atomic units).\
 For more details please read our \
article \n \" Arif Ullah, Luis E. Herrera Rodriguez, Pavlo O. Dral, and Alexei A. Kananenka, \
QD3SET-1: A Database woth Quantum Dissipative Dynamics Data sets https://doi.org/10.48550/arXiv.2301.12096\" \n ***************************************************************"
    return details

#%%%%%%%%%%%%%%---HEOM_FMO---%%%%%%%%%%%%

def heom_fmo_details(n_sites: int, authors: str, ref: str):
    details="\n **************************************************************** \n Calculations \
were performed for " + str(n_sites) + authors + ref + \
". To see the corresponding Hamiltonian, use the attribute, i.e,. output.H. \
Dynamics is propagated with the Hierarchical equation of motion (HEOM) approach [J. Chem. Theory Comput. 8,8,2808–2816 (2012)] \
implemented in the PHI package (version 1.0) [http://www.ks.uiuc.edu/Research/phi/]. In our calculations, \
the time-step for propagation was set to 0.1 fs and dynamics is propagated upto 2 ps.\
 Calculations are performed for initial excitation on site-1 case only.\
In calculations, we fixed a threshold 0.001. We kept changing K and/or L until the error \
went below the threshold or K and L become large enough so the\
calculation becomes intractably exceeding RAM available on our machines (1024 Gb).\n \n  The data \
and the corresponding parameters can be extracted as;  You can pass \
an extraction choice with keyword \"function(extr_choice: choice)\". \
The choice here is \'all\', \'site-1\' or \'cal_details\' \
which extracts data for the corresponding choice. The default choice is the 'cal_details' which \
provides details about the calculations. \n \n  From the output of the function, you can access the data \
as: \'output.data\' (for trajectories), \'output.N_trajs\' (to see the total number of trajectories), \
\'output.initial_site\' (to see the initial excited site), \'output.gamma\' (to see the cutoff \
frequencies for all trajectories), \'output.lamb\' (to see the system-bath coupling strengths for all trajectories) \
and the \'output.temp\' (to see th temperature values for all trajectories).  \n \n  It is worth-emphasizing that \'output.data\' is a dictionary and to extract the data, you can use \
\'xyz=list(output.data.values())\', where \'xyz[i]\' gives you the ith trajectory \
corresponding to the ith initial_site, gamma, lamb and  temp (all parameters are in cm^-1).\
 For more details please read our \
article \n \" Arif Ullah, Luis E. Herrera Rodriguez, Pavlo O. Dral, and Alexei A. Kananenka, \
QD3SET-1: A Database woth Quantum Dissipative Dynamics Data sets https://doi.org/10.48550/arXiv.2301.12096\" \n ***************************************************************"
    return details

#%%%%%%%%%%%%%%---LTLME_FMO---%%%%%%%%%%%%

def ltlme_fmo_details(n_sites: int, authors: str, ref: str):
    details = "\n **************************************************************** \n Calculations \
were performed for " + str(n_sites) + authors + ref + \
". To see the corresponding Hamiltonian, use the attribute, i.e,. output.H. \
Dynamics is propagated with the local thermalizing Lindblad master equation (LTLME) approach [J. Phys. Chem. Lett. 10, 7383-7390 (2019)] \
implemented in the quantum_HEOM package [https://github.com/jwa7/quantum_HEOM] with QuTip [https://qutip.org] \
in the backend. The basic quantum\_HEOM package is restricted to 7-site FMO complex.\
 In order to make it compatable for Hamiltonian with any dimension, we have made some local \
changes. In our calculations, the time-step for propagation was set to 5 fs and dynamics is propagated upto 50 ps.\n  The data \
and the corresponding parameters can be extracted as;  You can pass \
an extraction choice with keyword \"function(extr_choice: choice)\". \
The choice here is \'all\', \'site-1\', \'site-6\', \'site-8\' (in the case of 8-site FMO) or \'cal_details\' \
which extracts data for the corresponding choice. The default choice is the 'cal_details' which \
provides details about the calculations. \n \n From the output of the function, you can access the data \
as: \'output.data\' (for trajectories), \'output.N_trajs\' (to see the total number of trajectories), \
\'output.initial_site\' (to see the initial excited site), \'output.gamma\' (to see the cutoff \
frequencies for all trajectories), \'output.lamb\' (to see the system-bath coupling strengths for all trajectories) \
and the \'output.temp\' (to see th temperature values for all trajectories).  \n \n  It is worth-emphasizing that \'output.data\' is a dictionary and to extract the data, you can use \
\'xyz=list(output.data.values())\', where \'xyz[i]\' gives you the ith trajectory \
corresponding to the ith initial_site, gamma, lamb and  temp (all parameters are in cm^-1).\
 For more details please read our \
article \n \" Arif Ullah, Luis E. Herrera Rodriguez, Pavlo O. Dral, and Alexei A. Kananenka, \
QD3SET-1: A Database woth Quantum Dissipative Dynamics Data sets https://doi.org/10.48550/arXiv.2301.12096\" \n ***************************************************************"
    return details
