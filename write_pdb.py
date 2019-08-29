###################################################################
###				     				###
###	   		  RAMDout_to_PDB.py		  	###
### 		           ©Charlesmsa7				###
###							        ###
###################################################################

# This script will write PDB HETATM lines from the RAMD results. and
# creats a PDB structure 
# From the results text file, it extracts the specific coordinate 
# columns and convert it to float values
# Also you can get the file from user input

#####
#filname = input("Direction.txt ")
#Can be used to get input file(for future automations)
#####
filein = open("Direction.txt",'r')
outfile= open('Direction.pdb',"w")
#to write the atom numbers
#potein is too small, so initial no of atoms are 5000 to start HETATM section
#to avoid the clashes
#One can specify, if it was exactly known
atom = 1
for aline in filein.readlines():
	values = aline.split(" ")
#after splitting get the coloms contain coordinats of the center of ligand
#process and covert into desired format(float 8.3)
	#xval = float(values[-3])
	xval = (values[-3]).split(".") 
	xafd = (xval[1])
	#print(xafd) 
	x = (xval[0])+'.'+(xafd[0:3])
	#print(x)
	yval = values[-2]
	yval = (values[-2]).split(".")
	yafd = (yval[1])
	y = (yval[0])+'.'+(yafd[0:3])
	#print(y)
	zval = values[-1]
	zval = (values[-1]).split(".")
	zafd = (zval[1])
	z = (zval[0])+'.'+(zafd[0:3])
	#print(z)
	      #ATOM     66  OG  SER     5      40.084  24.201  38.718  1.00  0.00           O  	
	atom_str=str(atom) 
#Printing in the PDB format without compramise
#print in terminal(for verifcation) as well as file
# 6 5 1s 4 1 3 1s 4 1 3s 8 8 8 6 6 10s 2 2 \n
	#print("HETATM"+(atom_str.rjust(5," "))+' '+'  D'+"  "+'DUM'+" "+"  999"+"    "+x.rjust(8," ")+y.rjust(8," ")+z.rjust(8," ")+"  1.00  0.00           "+"D")
	outfile.write("HETATM"+(atom_str.rjust(5," "))+' '+'  D'+"  "+'DUM'+" "+"  999"+"    "+x.rjust(8," ")+y.rjust(8," ")+z.rjust(8," ")+"  1.00  0.00           "+"D\n")
	atom = atom + 1
#print("no of atoms" +str(atom))
#This segment will write the connect record for the available number of atoms

atom = atom-1 
print ("Number of atom atom "+str(atom))
for a1 in range(atom-1):
	a1 = a1+1	
	a2 = a1+1
	con1 = str(a1)
	con2 = str(a2)
	#print("CONECT"+con1.rjust(5, " ")+con2.rjust(5," "))
	outfile.write("CONECT"+con1.rjust(5, " ")+con2.rjust(5," ")+"\n")	
#add END record after the loop ends
outfile.write("END")
#after completion closes the file
filein.close()
