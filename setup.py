# This Python file uses the following encoding: utf-8
import os

from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

package_name = 'pyteos_nc'
setup(name=package_name,
      version="0.3",
      packages=find_packages(exclude=['test']),
      # metadata for upload to PyPI
      author="F. Laliberte",
      author_email="laliberte.frederic@utoronto.ca",
      description="This package provides command line tools to complement pyteos_air.",
      license="BSD",
      keywords="thermodynamics atmosphere climate",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Mathematics"],
      long_description=read('README.rst'),
      install_requires=['numpy>=1.6', 'netCDF4', 'scipy', 'psutil'],
      extras_require={'testing': ['flake8',
                                  'coverage',
                                  'pytest-cov',
                                  'pytest',
                                  'xarray'],
                      'recipes': ['click', 'pyteos_air>=1.0']},
      zip_safe=False,
      entry_points = {'console_scripts': [
                         'pyteos_nc = ' + package_name + '.netcdf_interface:main',
                         'pyteos_gen = ' + package_name + '.generators:generators']})
