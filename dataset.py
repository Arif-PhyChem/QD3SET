import methods as md


sb_choices = ['all', 'sym', 'asym', 'cal_details']
heom_fmo_choices = ['all', 'site-1', 'cal_details']
fmo7_choices = ['all', 'site-1', 'site-6', 'cal_details']
fmo8_choices = ['all', 'site-1', 'site-6', 'site-8','cal_details']
FMOtype = ['I', 'II']
FMOsites = [7, 8, 24]
system_choice = ['SB', 'FMO']
method_choice = ['HEOM', 'LTLME']
class qddset:
    """ Assign values to the parameters"""
    def __init__(self, **param):
        print('*****************************************')
        print('QD3SET-1 contains trajectories propagated for reduced density matrix of spin-boson model \
and FMO complex. Two methods were used: Local-thermalizing \
Lindblad Equation of Motion (LTLME) and Hierarachical \
Equations of Motion (HEOM). For more details, please read our \
article \" Arif Ullah, Luis E. Herrera Rodriguez, Pavlo O. Dral, and Alexei A. Kananenka, \
QDDSET-1: A Quantum Dissipative Dynamics Dataset\" \n *******************************************"') 

        if param.get('extr_choice') is not None:
            self._extr_choice = param.get('extr_choice')
            print('Running with the extraction choice "', self._extr_choice, '"')
        else:
            self._extr_choice = 'cal_details'
            print('As extraction choice is not provided, default extraction choice "cal_details" is used')
        if param.get('systemType') is not None:
            self._system = param.get('systemType')
            print('Extracting data for "', self._system, '"')
        else:
            self._system = 'SB'
            Print('As system type is not provided, default system choice "systemType: SB" is used')
        if param.get('methodType') is not None:
            self._method = param.get('methodType')
            print('Extracting data for "', self._method, '"')
        else:
            self._system = 'HEOM'
            print('As method type is not provided, default system choice "methodType: HEOM" is used')
        if param.get('dataPath') is not None:
            self._dataPath = param.get('dataPath')
            print('Extracting data from "', self._dataPath, '" directory')
        else:
            Print('Please provide the datapath using "dataPath"')
       
        if self._system == 'SB':
            assert self._extr_choice in sb_choices, (
                'As a string, need to pass either of these: extr_choice = \'all\', \'sym\', \'asym\' or \'cal_details\'')
        if self._system == 'FMO':
            if self._method == 'HEOM':
                assert self._extr_choice in heom_fmo_choices, (
                    'As a string, need to pass either of these: extr_choice = \'all\', \'site-1\' or \'cal_details\'')
            if self._method == 'LTLME':
                if self._system != 'FMO':
                    raise ValueError('In the case of LTLME method, only FMO data is provide thus systemType should be FMO')
            if param.get('Nsites') is not None:
                self._Nsites = param.get('Nsites')
                print('Extracting data for ', self._Nsites, 'sites FMO')
            else: 
                self._Nsites = 7
                print( 'Extracting data for ', self._Nsites, 'sites FMO(delf choice)')
            assert self._Nsites in FMOsites, (
                    'Number sites "Nsites" can be only equal to 7, 8 or 24')
            if self._Nsites == 24:
                self._FMOtype = 'I'
            else:
                if param.get('FMOtype') is not None:
                    self._FMOtype = param.get('FMOtype')
                    print('Extracting data for the  following FMO type "', self._FMOtype, '"')
                else:
                    self._FMOtype = 'I'
                    print('As FMO type is not provided, default choice "FMOtype: I" is used')
            assert self._FMOtype in FMOtype, (
                'FMOtype can be only I or II')
            if self._FMOtype == 'I':
                if self._Nsites == 7:
                    assert self._extr_choice in fmo7_choices, (
                    'As a string, need to pass either of these: extr_choice = \'all\', \'site-1\', \'site-6\' or \'cal_details\'')
                elif self._Nsites == 8:
                    assert self._extr_choice in fmo8_choices, (
                    'As a string, need to pass either of these: extr_choice = \'all\', \'site-1\', \'site-6\', \'site-8\', or \'cal_details\'')
            if self._FMOtype == 'II':
                if self._Nsites == 7:
                    assert self._extr_choice in fmo7_choices, (
                    'As a string, need to pass either of these: extr_choice = \'all\', \'site-1\', \'site-6\' or \'cal_details\'')
                elif self._Nsites == 8:
                    assert self._extr_choice in fmo8_choices, (
                    'As a string, need to pass either of these: extr_choice = \'all\', \'site-1\', \'site-6\', \'site-8\', or \'cal_details\'')
            if self._Nsites == 24:
                    assert self._extr_choice in fmo8_choices, (
                    'As a string, need to pass either of these: extr_choice = \'all\', \'site-1\', \'site-6\', \'site-8\', or \'cal_details\'')

    def extract(self):
        if self._system == 'SB':
            data = md.heom_sb(self._extr_choice, self._dataPath)
            return data
        if self._system == 'FMO':
            data = md.fmo_ltlme_heom(self._extr_choice, self._dataPath, self._FMOtype, self._method, self._Nsites)
            return data
