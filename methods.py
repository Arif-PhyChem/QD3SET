import os
import glob
import re
import numpy as np
from collections import namedtuple
import hamiltonians as hamil
import cal_details as cdet

def heom_sb(extr_choice: str, dataPath: str):
    """ Extracting HEOM data for spin boson"""
    if extr_choice == 'cal_details':
        details = cdet.heom_sb_details()
        H = ['epsilon', 'Delta', 'Delta*', '0']
        sbm = namedtuple('sbm', 'details H')
        sb = sbm(details, H)
    else: 
        data = {}
        # create empty list
        file_count = 0
        if extr_choice == 'all':
            datapath=dataPath + '/*'
            for files in glob.glob(datapath):
                file_count +=  1
        if extr_choice == 'sym':
            datapath=dataPath + '/*epsilon-0*'
            for files in glob.glob(datapath):
                file_count +=  1
        if extr_choice == 'asym':
            datapath=dataPath + '/*epsilon-1*'
            for files in glob.glob(datapath):
                file_count +=  1
        gamma = np.zeros((file_count), dtype=float)
        lamb = np.zeros((file_count), dtype=float)
        beta = np.zeros((file_count), dtype=float)
        epsilon = np.zeros((file_count), dtype=float)
        Delta = np.zeros((file_count), dtype=float)
        j = 0
        for files in glob.glob(datapath):
            file_name = os.path.basename(files)
            data[file_name] = np.load(files)
            #
            # extract the values of gamma, lambda and temperature from the file name
            #
            file_name = os.path.basename(files)
            x = re.split(r'-', file_name)
            y = re.split(r'_', x[1])
            epsilon[j] = y[0]
            y = re.split(r'_', x[2])
            Delta[j] = y[0]
            y = re.split(r'_', x[3])
            lamb[j] = y[0]
            y = re.split(r'_', x[4])
            gamma[j] = y[0]
            y = re.split(r'.n', x[5])
            beta[j] = y[0]
            j += 1
        details = cdet.heom_sb_details()
        H = ['epsilon', 'Delta', 'Delta*', '0']
        sbm = namedtuple('sbm', 'details H N_trajs epsilon Delta gamma lamb beta data')
        sb = sbm(details, H, file_count, epsilon, Delta, gamma, lamb, beta, data)
    return sb 
##################################
#  Extract FMO data 
##################################
def fmo_ltlme_heom(extr_choice: str, dataPath: str, FMOtype: str, method: str, Nsites: int):
    if method == 'LTLME':
        if FMOtype == 'I':
            if Nsites == 7:
                details = cdet.ltlme_fmo_details(7, '-site FMO complex parametrized by Adolphs and Renger', ' [Biophys. J. 91, 2778 (2006)]')
                H = hamil.adolphs_renger()
            if Nsites == 8:
                details = cdet.ltlme_fmo_details(8, '-site FMO complex parametrized by Olbrich et. al.', ' [J. Phys. Chem. B 115, 8609 (2011)]')
                H = hamil.olbrich_et_al()
        if FMOtype == 'II':
            if Nsites == 7:
                details = cdet.ltlme_fmo_details(7, '-site FMO complex parametrized by Cho et. al.', ' [J. Phys. Chem. B 109, 10542 (2005)]')
                H = hamil.cho_et_al()
            if Nsites == 8:
                details = cdet.ltlme_fmo_details(8, '-site FMO complex parametrized by Jia et. al.', ' [Sci. Rep. 5, 17096 (2015)]')
                H = hamil.jia_et_al()
        if Nsites == 24:
            details = cdet.ltlme_fmo_details(24, '-site FMO trimer with Hamiltonian given in [J. Chem. Theory Comput. 2015, 11, 3411−3419] and ', '[J. Chem. Phys. 145, 024101 (2016)]')
            H = hamil.fmo_trimer()
    if method == 'HEOM':
        details = cdet.heom_fmo_details(8, '-site FMO complex parametrized by Olbrich et. al.', ' [J. Phys. Chem. B 115, 8609 (2011)]')
        H = hamil.olbrich_et_al()
    if extr_choice == 'cal_details':
        fmo = namedtuple('fmo', 'details H')
        fmo = fmo(details, H)
    else: 
        data = {}
        # create empty list
        file_count = 0
        if extr_choice == 'all':
            datapath=dataPath + '/*'
            for files in glob.glob(datapath):
                file_count +=  1
        if extr_choice == 'site-1':
            datapath=dataPath + '/*initial-1*'
            for files in glob.glob(datapath):
                file_count +=  1
        if extr_choice == 'site-6':
            datapath=dataPath + '/*initial-6*'
            for files in glob.glob(datapath):
                file_count +=  1
        if extr_choice == 'site-8':
            datapath=dataPath + '/*initial-8*'
            for files in glob.glob(datapath):
                file_count +=  1
        gamma = np.zeros((file_count), dtype=float)
        lamb = np.zeros((file_count), dtype=float)
        temp = np.zeros((file_count), dtype=float)
        initial = np.zeros((file_count), dtype=int)
        j = 0
        for files in glob.glob(datapath):
            file_name = os.path.basename(files)
            data[file_name] = np.load(files)
            #
            # extract the values of gamma, lambda and temperature from the file name
            #
            x = re.split(r'_', file_name)
            y = re.split(r'-', x[1])
            initial[j] = y[1]
            y = re.split(r'-', x[2]) # extracting value of gamma
            gamma[j] = y[1] 
            y = re.split(r'-', x[3]) # extract value of lambda 
            lamb[j] = y[1]
            y = re.split(r'-', x[4]) 
            x = re.split(r'.npy', y[1]) # extract value of temperature
            temp[j] = x[0]
            j = j + 1
        fmocomplex = namedtuple('fmocomplex', 'details H N_trajs initial_site gamma lamb temp data')
        fmo = fmocomplex(details, H, file_count, initial, gamma, lamb, temp, data)
    return fmo 
