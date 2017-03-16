"""
    Test the table generator.
"""

import numpy as np
import os
from netCDF4 import Dataset
from argparse import Namespace
import xarray as xr
import datetime

from pyteos_nc.generators.pottemps import compute_pottemps
from pyteos_nc.netcdf_interface import create_thermo


def test_interface_pottemp(tmpdir):
    compute_pottemps(tmpdir.strpath, 1, True)
    tmpdir_files = [fn.basename for fn in tmpdir.listdir()]
    args = Namespace(in_thermodynamic_file=tmpdir.join('massfraction_air_pottemp_g_ref_common_pressures.dat').strpath,
                     in_netcdf_file=tmpdir.join('in.nc').strpath,
                     out_netcdf_file=tmpdir.join('out.nc').strpath,
                     zlib=False, memory_percent=0.01)
    ds = xr.Dataset({'ta': (['time', 'plev', 'lat', 'lon'], np.array(300).reshape((1, 1, 1, 1))),
                     'pa': (['time', 'plev', 'lat', 'lon'], np.array(5e4).reshape((1, 1, 1, 1))),
                     'hus': (['time', 'plev', 'lat', 'lon'], np.array(1.0 - 0.98).reshape((1, 1, 1, 1)))},
                    coords={'time': [datetime.datetime(2000, 1, 1)],
                            'plev': [5e4],
                            'lat': [45.0],
                            'lon': [0.0]})
    ds.to_netcdf(args.in_netcdf_file)

    create_thermo(args)
    with Dataset(args.out_netcdf_file) as output:
        np.testing.assert_allclose(output.variables['pottemp'][:].squeeze(), 365.2154567609769, atol=1.0)
                     

def test_interface_pottempequiapprox(tmpdir):
    compute_pottemps(tmpdir.strpath, 1, True)
    tmpdir_files = [fn.basename for fn in tmpdir.listdir()]
    args = Namespace(in_thermodynamic_file=tmpdir.join('massfraction_air_pottempequiapprox_g_ref_common_pressures.dat').strpath,
                     in_netcdf_file=tmpdir.join('in.nc').strpath,
                     out_netcdf_file=tmpdir.join('out.nc').strpath,
                     zlib=False, memory_percent=0.01)
    ds = xr.Dataset({'ta': (['time', 'plev', 'lat', 'lon'], np.array(300).reshape((1, 1, 1, 1))),
                     'pa': (['time', 'plev', 'lat', 'lon'], np.array(5e4).reshape((1, 1, 1, 1))),
                     'hus': (['time', 'plev', 'lat', 'lon'], np.array(1.0 - 0.98).reshape((1, 1, 1, 1)))},
                    coords={'time': [datetime.datetime(2000, 1, 1)],
                            'plev': [5e4],
                            'lat': [45.0],
                            'lon': [0.0]})
    ds.to_netcdf(args.in_netcdf_file)

    create_thermo(args)
    with Dataset(args.out_netcdf_file) as output:
        np.testing.assert_allclose(output.variables['pottempequiapprox'][:].squeeze(), 440.05599314639227, atol=1.0)
