#!/bin/bash

# RUN THIS IN THE STARTING DIRECTORY OF THE CRYSPY JOB

### Header ###

# This is the stage 3 script

### MAIN ###

# This python script generates a density vs energy plot of the lammps results
# It also generates the QE input and an easy to run bash script

lammps_to_QE_ob86.py

echo Stage 3 complete

### END ###
