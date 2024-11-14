#!/usr/bin/env python3

### Import modules ###

from matplotlib import pyplot

import os

### Directory names ###

dirs = []

dir_file = "manual_dft_submission"

for line in open(dir_file, 'r').readlines():
    if 'cd work' in line:
        dirs.append(line.split()[1])
        
print(dirs)
    
### Read energies and densities ###

ex_ens = []
ex_rhos = []

for entry in dirs:
    ind = entry
    ofile = entry + "/pwscf.out"
    
    print(ofile)

    rho = -1.0
    en = -1.0
    
    dft_data = open(ofile, 'r').readlines()
    
    if 'JOB DONE' in dft_data[-2]:
    
        for line in dft_data:
        
            # find the last density entry in the file
            
            if 'density =' in line:
            
                rho = float(line.split()[2])
                
            if 'total energy' in line:
            
                if line.split()[3] != 'Ry':
                
                    # print(line.split()) # For debugging
                    en = float(line.split()[3])
                    
    else:
    
        print("Calculation Not Converged")
        print(ofile)
        print("\n")

    ex_rhos.append(rho)
    ex_ens.append(en)
    
print(ex_rhos)
print("\n")
print(ex_ens)

### Do plots

# Get user input for Crystal Structure benchmark

print("Please provide reference energy: ")

minen = float(input())

ex_ens = [en / 13.605704 for en in ex_ens]

ex_ens = [en - minen for en in ex_ens]

print("Do you want absolute rho (yes/no)?: ")

abs_request = input()

rhos = []

if abs_request == "yes":
   
    for rho in ex_rhos:
   
        rhos.append(ex_rhos[rho])
   
	
else:

    for rho in ex_rhos:
   
        rhos.append(ex_rhos[rho])
   
        print("Please provide reference density: ")
   
        minrho = float(input())
   
        rhos = [rho - minrho for rho in rhos]
 
pyplot.scatter(ex_ens, rhos, c="blue", alpha=0.5)
pyplot.xlabel('Rel. energy per atom (eV)')
   
if abs_request == "yes":   
   
    pyplot.ylabel('Density (g / cm3)')
   
else:

    pyplot.ylabel('Rel. density (g / cm3)')

#pyplot.show()
pyplot.savefig('dft_rho_en.png')

print("Density vs Energy Graph Generated")

### Output structure list with energies and densities ###
    
print("Would you like to generate a Structure ID and Energy data file? (yes/no)")
    
out_choice = input()
    
if out_choice == "yes":
    
    # Set filename variables
    
    dft_table = "DFT_output"
    	
    os.mkdir(dft_table)
    	
    table_file = "DFT_output/tabulated_data"
    
    # Get list of target directories
    
    print_ctr = len(dirs)
    
    # os.mkdir(dft_results)
    
    bash_file = "get_dft_structures"
    
    ids = []
    
    for id in range(0, print_ctr):
    
    	structure_id = dirs[id].split("/")[2]
    	
    	ids.append(structure_id)
    	
    	structure_dir = "DFT_output/" + structure_id
    	
    	os.mkdir(structure_dir)
    	
    	with open(bash_file, 'a+') as bash_f:
        
            position = dirs[id] + "/pwscf.out" 
            destination = structure_dir
            cp_cmd = "cp " + position + " " + destination
            bash_f.write(cp_cmd)
            bash_f.write("\n")
            
            bash_f.close()
    	
    # Create file
    
    with open(table_file, 'a+') as f:
     
     	# Print file header
     	
     	f.write("Structure ID     Energy per atom (eV)     Density\n")
     	
     	for struc in range(0, print_ctr):
     	    data_string = ids[struc] + "   " + ex_ens[struc] + "   " + rhos[struc]
     	    f.write(data_string)
     	f.close()    
    
### END ###    
