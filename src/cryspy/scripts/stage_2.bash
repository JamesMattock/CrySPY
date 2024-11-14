#!/bin/bash

### Header ###

# This is the stage 2 script
# It creates and builds the CrySPY run with LAMMPS
# It extracts the partial charges calculated from stage 1

### Main ###

# Create a directory to work in
# This keeps the CrySPY directory clean

mkdir generation
cd generation

# Python script extracts data from the charge output file
# This is the LAMMPS input file creation script
# This will need to create a P1 CIF for the LAMMPS interface

# Create dummy cryspy run to approximate a P1 crystal structure

mkdir dummy_cryspy
cd dummy_cryspy

cp ../../*.xyz .

write_cryspy_dummy.py 

# Run the dummy CrySPY job

cryspy

# Retrieve the CIF for the LAMMPS interface
# IT MUST BE P1
# CrySPY stores the input and output structures as pymatgen structure objects in pickle files

cd data/pkl_data

unpickle_dummy.py

# Dummy file is called p1_structure.cif

# Python script extracts data from the charge output file
# This is the LAMMPS potential file expansion script
# It will require a file from LAMMPS Interface

cd ../../../../
mkdir calc_in
cd calc_in

cp ../generation/dummy_cryspy/data/pkl_data/p1_structure.cif .

conda run -n lammps_file_create lammps-interface -ff UFF --minimize --replication 1x1x1 p1_structure.cif

cp data.p1_structure data.potentials

write_lammps_runscript.py

modify_lammps_input.py

extract_charges.py

# Create the cryspy.in input file

cd ../

# Create the CrySPY input file

write_cryspy_input.py

echo Stage 2 complete

### END ###
