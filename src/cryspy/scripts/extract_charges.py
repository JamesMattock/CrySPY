#!/usr/bin/env python3

### Header ###

# This script extracts the charges from the Gaussian jobs

# It is included in stage 2

### Import modules ###

### Main ###

# List of xyz file paths needed for input
# Number of each molecule is also needed

filename = "../molelist"

moledata = open(filename, 'r').readlines()

molenames = []
molnums = []
mollengths = []

for line in moledata:

    moledata_line = line.split()
    
    if len(moledata_line) > 0:
    
        molenames.append(moledata_line[1])
        molnums.append(moledata_line[0])

# Get the charges from the extracted Mulliken charges
# Save the charges to an array so the file doesn't have to remain open

charge_files = []

for molecule in molenames:

    molecule.rstrip()
    dir_name = molecule.rstrip(".xyz")
    charge_file = dir_name + "/charges.log"
    
    charge_files.append(charge_file)
    
mol_number = 0

collated_data = []
    
for file in charge_files:

    file = "../" + file

    charge_text = open(file, 'r').readlines()
    
    # print(charge_text[-1]) # For debugging 
    
    line_num_var = 0
    
    for line in charge_text:
    
        if "Mulliken charges:" in line:
        
            line_index = charge_text.index(line)
        
            line_num_var = line_index
            # print(line_num_var) # For debugging 
            
    for data_line in range(line_num_var, len(charge_text)):
    
        if len(charge_text[data_line].split()) < 5:
    
            collated_data.append(charge_text[data_line])
            
        else:
        
            break
    
    mol_number = mol_number + 1

# Save charge data to file

collated_file = "../generation/charge_output.text"
    
col = open(collated_file, "w")
col.writelines(collated_data)
col.close()

### End ###
