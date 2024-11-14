#!/usr/bin/env python3

### Header ###

# This script extracts the data from a dummy CrySPY job
# It is designed to create a single P1 structure
# This is to allow for the running of LAMMPS interface
# The output data is pickled
# The python objects in this case are pymatgen structures

# It is included in stage 2

### Import modules ###

import pickle
from pymatgen.io.cif import CifWriter

### Main ###

# Unpickle the initial structures

filename = 'init_struc_data.pkl'

with open(filename, 'rb') as f_1:
    
    init_struc_data = pickle.load(f_1)
    
results_file = 'p1_structure.cif'

# Use pymatgen CifWriter to create a cif output from the structure object

results_output = CifWriter(init_struc_data[0])

# Write results to file

results_output.write_file(results_file)

### END ###
