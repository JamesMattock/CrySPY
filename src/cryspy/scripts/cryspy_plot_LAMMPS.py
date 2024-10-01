#!/usr/bin/env python3

### Header ###

# This script reads the LAMMPS output from a CrySPY run
# It calculates densities from the molecular weight and the cell volume
# It generates density vs relative energy plots

### Import modules ###

from matplotlib import pyplot

### Create tools ###

def isfloat(num):
    
    try:
        float(num)
        return True
    except ValueError:
        return False

### Read minimised energies and cell volumes ###

# Get user input filename
# This should be the logfile specificed in LAMMPS interface

print("Please enter name of logfile: ")
logfile = input()

print("Please enter Molecular Weight of Unit Cell: ")
mr = float(input())

print("Please enter the number of atoms in the unit cell")
num_of_atoms = float(input())

print("Please enter number of structures generated: ")
struc_ctr = int(input())

data_rho = []
data_en = []

for entry in range(0, struc_ctr):

    directory = 'work/fin/%06i/'%entry
    
    ofile = directory + logfile

    print(ofile) # For debugging
    
    output = open(ofile, 'r').readlines()
    
    loop_ctr = len(output)

    vol = -1.0
    tot_en = -1.0

    trash = 1.0 # Don't ask
    
    for line in range(0, loop_ctr):
        # find the last density entry in the file

       if len(output[line].split()) != 7:

            trash = 1.1

       else:
	
            if output[line].split()[6] == 'Volume':
                vol_line = output[line + 2]

                if isfloat(vol_line.split()[6]) == True:

                    vol = float(vol_line.split()[6])
                    tot_en = float(vol_line.split()[4])
    
    # Calculate density and convert from Mr/A3 to g/cm3
    
    if vol != -1.0:         
        
        rho = (mr / vol) * 1.660578
    
        # Calculate energy per atom and convert from kcal/mol to eV
    
        atom_en = (tot_en / 23.06) / num_of_atoms

        data_rho.append(rho)
        data_en.append(atom_en)

### Plot graphs ###

# This for loop is designed to remove outliers
# Modify value as applicable

for result in data_en:

    if result > 1.0:

       rem = data_en.index(result)

       del data_en[rem]
       del data_rho[rem]

ens = []

data_en_ctr = len(data_en)

print("Number of energies\n") # For debugging
print(data_en_ctr) # For debugging
print(data_en) # For debugging
print("\n") # For debugging0

for entry_en in range(0, data_en_ctr):

    ens.append(data_en[entry_en])

# Get user input for Crystal Structure bechmark

print("Do you want absolute energy (yes/no)?: ")

abs_en_request = input()

if abs_en_request == "no":

    print("Please provide reference energy: ")

    minen = float(input())

    ens = [en_save - minen for en_save in ens]
    
else:

    minen = min(ens)
    
    ens = [en_save - minen for en_save in ens]

print("The ens array") # For debugging
print(ens) # For debugging

print("Do you want absolute rho (yes/no)?: ")

abs_request = input()

data_rho_ctr = len(data_rho)

print("Number of densities\n") # For debugging
print(data_rho_ctr) # For debugging
print(data_rho) # For debugging
print("\n") # For debugging

if abs_request == "yes":

   rhos = []
   
   for entry_rho in range(0, data_rho_ctr):
   
       rhos.append(data_rho[entry_rho])
	
else:

   rhos = []
   
   for entry_rho in range(0, data_rho_ctr):
   
       rhos.append(data_rho[entry_rho])
   
   print("Please provide reference density: ")
   
   minrho = float(input())
   
   rhos = [rho_save - minrho for rho_save in rhos]

# spg = [2 * entry['Sgp_num'] for entry in data]

print("The rhos array") # For debugging
print(rhos) # For debugging

# This for loop is designed to remove outliers
# Modify value as applicable

#for result in ens:
#
#   if result > 1.0:
#
#       rem = ens.index(result)
#
#      del ens[rem]
#      del rhos[rem]
 
pyplot.scatter(ens, rhos, c="Blue", alpha=0.5)
pyplot.xlabel('Rel. energy per atom (eV)')
   
if abs_request == "yes":   
   
   pyplot.ylabel('Density (g / cm3)')
   
else:

   pyplot.ylabel('Rel. density (g / cm3)')

#pyplot.show()
pyplot.savefig('rho_en.png')

print("Thank you for choosing us to generate your output, have a nice day!")

### End ###
