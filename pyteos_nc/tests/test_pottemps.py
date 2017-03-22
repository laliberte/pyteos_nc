"""
    Test the table generator.
"""

import numpy as np
import os
from contextlib import closing

from pyteos_nc.generators.pottemps import compute_pottemps


def test_create_table_exact(tmpdir):
    compute_pottemps(tmpdir.strpath, 1, True, False)
    tmpdir_files = [fn.basename for fn in tmpdir.listdir()]
    assert 'massfraction_air_pottempequi_g_ref_common_pressures.dat' in tmpdir_files
    assert 'massfraction_air_pottemp_g_ref_common_pressures.dat' in tmpdir_files


def test_create_table_approx(tmpdir):
    compute_pottemps(tmpdir.strpath, 1, True, True)
    tmpdir_files = [fn.basename for fn in tmpdir.listdir()]
    assert 'massfraction_air_pottempequiapprox_g_ref_common_pressures.dat' in tmpdir_files
    assert 'massfraction_air_pottemp_g_ref_common_pressures.dat' in tmpdir_files
