import click
from .pottemps import compute_pottemps

@click.group()
def generators():
    return

@generators.command()
@click.argument('dest_dir')
@click.option('--num_procs', type=int,
              default=1,
              help="Number of processes to use. Default: 1.")
@click.option('--test', is_flag=True,
              help="Simple testing. Create a much less precise table.")
def pottemps(dest_dir, num_procs, test):
    """
    This script computes two data files:
        DEST_DIR/massfraction_air_pottempequiapprox_g_ref_common_pressures.dat  
        DEST_DIR/massfraction_air_pottemp_g_ref_common_pressures.dat

    that can be used with the pyteos_nc compute to compute moist air
    equivalent potential temperature and dry (virtual) potential temperature,
    respectively, from CF-compliants netcdf files:

    For example,

    $ pyteos_nc DEST_DIR/massfraction_air_pottempequiapprox_g_ref_common_pressures.dat in.nc out.nc

    would compute pottempequiapprox, the approximate equivalent potential temperature, from file in.nc and
    store the result in out.nc.

    In this example, in.nc should contain variables ta (air temperature),
    hus (specific humidity) and air pressure (pa).
    """
    compute_pottemps(dest_dir, num_procs, test)
