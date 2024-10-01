#!/usr/bin/env python3

# Code to integrate LAMMPS with CrySPY
# Reaxff requires charges in the atom specification

import os

# Filename should be the same everytime
filename = "lammps.lattice.dat"

with open(filename, 'r') as f:

    text = f.readlines()
    atoms_line = 0

    for line in text:
        if line.find('Atoms') != -1:
            atoms_line = text.index(line)

    final_line = len(text)
    #print(atoms_line)
    #print(final_line)

    for coord in range((atoms_line + 2), final_line):

        coord_line = text[coord].split()
        #print(coord_line) # For debugging

        # coord_line.insert(2, ' 0.0 ')
        
        # Hydrogen partial charges
        
        if coord == (atoms_line + 2) or coord == (atoms_line + 8) or coord == (atoms_line + 14) or coord == (atoms_line + 20):
        
        	coord_line.insert(2, ' 0.268850 ')
        	
        elif coord == (atoms_line + 3) or coord == (atoms_line + 9) or coord == (atoms_line + 15) or coord == (atoms_line + 21):
        
        	coord_line.insert(2, ' 0.268850 ')
        	
        elif coord == (atoms_line + 4) or coord == (atoms_line + 10) or coord == (atoms_line + 16) or coord == (atoms_line + 22):
        
        	coord_line.insert(2, ' 0.220062 ')
        	
        elif coord == (atoms_line + 5) or coord == (atoms_line + 11) or coord == (atoms_line + 17) or coord == (atoms_line + 23):
        
        	coord_line.insert(2, ' 0.199775 ')
        	
        elif coord == (atoms_line + 6) or coord == (atoms_line + 12) or coord == (atoms_line + 18) or coord == (atoms_line + 24):
        
        	coord_line.insert(2, ' 0.253800 ')
        	
        elif coord == (atoms_line + 7) or coord == (atoms_line + 13) or coord == (atoms_line + 19) or coord == (atoms_line + 25):
        
        	coord_line.insert(2, ' 0.220062 ')
        
        # Carbon partial charges
        	
        elif coord == (atoms_line + 26) or coord == (atoms_line + 32) or coord == (atoms_line + 38) or coord == (atoms_line + 44):
        
        	coord_line.insert(2, ' -0.225758 ')
        	
        elif coord == (atoms_line + 27) or coord == (atoms_line + 33) or coord == (atoms_line + 39) or coord == (atoms_line + 45):
        
        	coord_line.insert(2, ' -0.239290 ')
        	
        elif coord == (atoms_line + 28) or coord == (atoms_line + 34) or coord == (atoms_line + 40) or coord == (atoms_line + 46):
        
        	coord_line.insert(2, ' -0.120205 ')
        	
        elif coord == (atoms_line + 29) or coord == (atoms_line + 35) or coord == (atoms_line + 41) or coord == (atoms_line + 47):
        
        	coord_line.insert(2, ' -0.042520 ')
        	
        elif coord == (atoms_line + 30) or coord == (atoms_line + 36) or coord == (atoms_line + 42) or coord == (atoms_line + 48):
        
        	coord_line.insert(2, ' -0.174000 ')
        	
        elif coord == (atoms_line + 31) or coord == (atoms_line + 37) or coord == (atoms_line + 43) or coord == (atoms_line + 49):
        
        	coord_line.insert(2, ' -0.042520 ')
        	
        # Nitrogen partial charges
        
        elif coord == (atoms_line + 50) or coord == (atoms_line + 62) or coord == (atoms_line + 74) or coord == (atoms_line + 86):
        
        	coord_line.insert(2, ' 0.082426 ')
        	
        elif coord == (atoms_line + 51) or coord == (atoms_line + 63) or coord == (atoms_line + 75) or coord == (atoms_line + 87):
        
        	coord_line.insert(2, ' 0.654737 ')
        	
        elif coord == (atoms_line + 52) or coord == (atoms_line + 64) or coord == (atoms_line + 76) or coord == (atoms_line + 88):
        
        	coord_line.insert(2, ' 0.082426 ')
        	
        elif coord == (atoms_line + 53) or coord == (atoms_line + 65) or coord == (atoms_line + 77) or coord == (atoms_line + 89):
        
        	coord_line.insert(2, ' 0.647012 ')
        	
        elif coord == (atoms_line + 54) or coord == (atoms_line + 66) or coord == (atoms_line + 78) or coord == (atoms_line + 90):
        
        	coord_line.insert(2, ' -0.034598 ')
        	
        elif coord == (atoms_line + 55) or coord == (atoms_line + 67) or coord == (atoms_line + 79) or coord == (atoms_line + 91):
        
        	coord_line.insert(2, ' 0.647012 ')
        	
        elif coord == (atoms_line + 56) or coord == (atoms_line + 68) or coord == (atoms_line + 80) or coord == (atoms_line + 92):
        
        	coord_line.insert(2, ' -0.052662 ')
        	
        elif coord == (atoms_line + 57) or coord == (atoms_line + 69) or coord == (atoms_line + 81) or coord == (atoms_line + 93):
        
        	coord_line.insert(2, ' 0.685266 ')
        	
        elif coord == (atoms_line + 58) or coord == (atoms_line + 70) or coord == (atoms_line + 82) or coord == (atoms_line + 94):
        
        	coord_line.insert(2, ' -0.061824 ')
        	
        elif coord == (atoms_line + 59) or coord == (atoms_line + 71) or coord == (atoms_line + 83) or coord == (atoms_line + 95):
        
        	coord_line.insert(2, ' 0.685266 ')
        	
        elif coord == (atoms_line + 60) or coord == (atoms_line + 72) or coord == (atoms_line + 84) or coord == (atoms_line + 96):
        
        	coord_line.insert(2, ' -0.059249 ')
        	
        elif coord == (atoms_line + 61) or coord == (atoms_line + 73) or coord == (atoms_line + 85) or coord == (atoms_line + 97):
        
        	coord_line.insert(2, ' 0.647012 ')
        	
        # Oxygen partial charges
        
        elif coord == (atoms_line + 98) or coord == (atoms_line + 110) or coord == (atoms_line + 122) or coord == (atoms_line + 134):
        
        	coord_line.insert(2, ' -0.377260 ')
        	
        elif coord == (atoms_line + 99) or coord == (atoms_line + 111) or coord == (atoms_line + 123) or coord == (atoms_line + 135):
        
        	coord_line.insert(2, ' -0.377260 ')
        	
        elif coord == (atoms_line + 100) or coord == (atoms_line + 112) or coord == (atoms_line + 124) or coord == (atoms_line + 136):
        
        	coord_line.insert(2, ' -0.377260 ')
        	
        elif coord == (atoms_line + 101) or coord == (atoms_line + 113) or coord == (atoms_line + 125) or coord == (atoms_line + 137):
        
        	coord_line.insert(2, ' -0.377260 ')
        	
        elif coord == (atoms_line + 102) or coord == (atoms_line + 114) or coord == (atoms_line + 126) or coord == (atoms_line + 138):
        
        	coord_line.insert(2, ' -0.369904 ')
        	
        elif coord == (atoms_line + 103) or coord == (atoms_line + 115) or coord == (atoms_line + 127) or coord == (atoms_line + 139):
        
        	coord_line.insert(2, ' -0.369904 ')
        	
        elif coord == (atoms_line + 104) or coord == (atoms_line + 116) or coord == (atoms_line + 128) or coord == (atoms_line + 140):
        
        	coord_line.insert(2, ' -0.380318 ')
        	
        elif coord == (atoms_line + 105) or coord == (atoms_line + 117) or coord == (atoms_line + 129) or coord == (atoms_line + 141):
        
        	coord_line.insert(2, ' -0.380318 ')
        	
        elif coord == (atoms_line + 106) or coord == (atoms_line + 118) or coord == (atoms_line + 130) or coord == (atoms_line + 142):
        
        	coord_line.insert(2, ' -0.380318 ')
        	
        elif coord == (atoms_line + 107) or coord == (atoms_line + 119) or coord == (atoms_line + 131) or coord == (atoms_line + 143):
        
        	coord_line.insert(2, ' -0.380318 ')
        	
        elif coord == (atoms_line + 108) or coord == (atoms_line + 120) or coord == (atoms_line + 132) or coord == (atoms_line + 144):
        
        	coord_line.insert(2, ' -0.369904 ')
        	
        elif coord == (atoms_line + 109) or coord == (atoms_line + 121) or coord == (atoms_line + 133) or coord == (atoms_line + 145):
        
        	coord_line.insert(2, ' -0.369904 ')
        	
        coord_line.insert(1, ' 1 ')
        
        save_coords = str(coord_line[0] + ' ' + coord_line[1] + ' ' + coord_line[2] + ' ' + coord_line[3] + ' ' + \
                      coord_line[4] + ' ' + coord_line[5] + ' ' + coord_line[6] + '\n')

        #print(save_coords) # For debugging
        text[coord] = save_coords
    #f.close()

# Insert more header lines
# WARNING - this is hard coded at the moment
# Let's not kid ourselves and pretend like I'm going to remember to change it


text.insert(4, '156 bonds\n')
text.insert(5, '288 angles\n')
text.insert(6, '492 dihedrals\n')
text.insert(7, '144 impropers\n')
text.insert(8, '\n')
text.insert(10, '5 bond types\n')
text.insert(11, '8 angle types\n')
text.insert(12, '3 dihedral types\n')
text.insert(13, '1 improper types\n')
text.insert(14, '\n')

# Delete existing file
os.remove(filename)

final_line = len(text)

# recreate with new data
with open(filename, 'w') as f:
    #print(len(text))
    for new_line in range(0, final_line):
        #print(text[new_line])
        f.write(text[new_line])

    #f.close()
