# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
A Python package for the quantitative analysis of the interaction of energetic
photons with matter (x-rays and gamma-rays).
"""
import os
from astropy.io import ascii
from astropy.table import QTable
import astropy.units as u
# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    _package_directory = os.path.dirname(os.path.abspath(__file__))
    _data_directory = os.path.abspath(os.path.join(_package_directory, 'data'))

    elements_file = os.path.join(_data_directory, 'elements.csv')
    elements = QTable(ascii.read(elements_file, format='csv'))

    elements['density'].unit = u.g / (u.cm ** 3)
    elements['i'].unit = u.eV
    elements['ionization energy'].unit = u.eV
    elements['atomic mass'] =  elements['z'] / elements['zovera'] * u.u
    elements.add_index('symbol')

    compounds_file = os.path.join(_data_directory, 'compounds_mixtures.csv')
    compounds = QTable(ascii.read(compounds_file,
                                  format='csv', fast_reader=False))
    compounds['density'].unit = u.g / (u.cm ** 3)
    # compounds.add_index('symbol')

    emission_energies_file = os.path.join(_data_directory,
                                          'emission_energies.csv')
    emission_energies = QTable(ascii.read(emission_energies_file))
    for colname in emission_energies.colnames[2:]:
        emission_energies[colname].unit = u.eV
