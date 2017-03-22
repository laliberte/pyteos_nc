#Standard packages:
import pickle
import numpy as np
from pyteos_air import liq_ice_air
from pyteos_air.pyteos_interface import create_gridded_data

#Specific packages:
from ..create_interpolants import Interpolated_data

def compute_pottemps(dest_dir, num_procs, test, approx):
    """
    This script computes two data files:
        DEST_DIR/massfraction_air_pottempequi_g_ref_common_pressures.dat  
        DEST_DIR/massfraction_air_pottemp_g_ref_common_pressures.dat
    """
    name = 'common_pressures'
    if test:
        thermo_axes = {'rh_wmo': np.linspace(0, 2.0, 11),
                       'T': np.linspace(150, 330, 10),
                       'p': np.array([1.0, 100.0, 500.0,850.0,1000.0])*1e2}
    else:
        thermo_axes = {'rh_wmo': np.linspace(0, 2.0, 101),
                       'T': np.linspace(150, 330, 181),
                       'p': np.array([1.0, 10.0, 50.0, 100.0, 150.0, 200.0, 250.0, 300.0,
                                      400.0,500.0,600.0,700.0,850.0,925.0,1000.0])*1e2}
    thermo_axes['pref'] = 1e5
    if approx:
        compute_pottemp('pottempequiapprox', num_procs, thermo_axes, name, dest_dir)
    else:
        compute_pottemp('pottempequi', num_procs, thermo_axes, name, dest_dir)
    compute_pottemp('pottemp', num_procs, thermo_axes, name, dest_dir)


def compute_massfraction_air(num_procs, thermo_axes):
    thermo_axes_massfrac = {'T': thermo_axes['T'],
                            'p': thermo_axes['p']}
    thermo_data = create_gridded_data(liq_ice_air, 'sat', 'massfraction_air',
                                      thermo_axes_massfrac, num_procs=num_procs)
    return Interpolated_data(liq_ice_air, 'sat', 'massfraction_air', thermo_axes_massfrac,
                             thermo_data)


def compute_pottemp(pottempname, num_procs, thermo_axes, name, dest_dir):
    func_list = {}
    functions=[pottempname]
    realm='g_ref'

    for function in functions:
        thermo_data = create_gridded_data(liq_ice_air,realm,function,thermo_axes,num_procs=num_procs)
        func_list[function] = Interpolated_data(liq_ice_air,realm,function,thermo_axes,thermo_data)

    func_list['massfraction_air'] = compute_massfraction_air(num_procs, thermo_axes)

    with open(dest_dir+'/'+'_'.join(sorted(list(func_list.keys()))) +
              '_' + realm + '_' + name + '.dat', 'wb') as file:
        pickle.dump(func_list,file)


if __name__=='__main__':
    compute_thermo()
