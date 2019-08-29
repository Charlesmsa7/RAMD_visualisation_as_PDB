#/bin/bash
#Be clear cefore running the program about the path for structure file
structure_path=/home/user01/Charles/Program
grep -v -e 'WAT' -e 'Na+' -e 'Cl-' -e 'END' ${structure_path}/lastframe.pdb > temp.pdb

#

for d in */ ; do
	cd $d
	out=$d
	echo "Directory is ${out}"
	grep "LIGAND COM is" *.out > Direction.txt
	dir_fname=`echo *.out | cut -d '.' -f1`
	echo "${dir_fname}"
# Execution of the python_script from the parent folder(master program-no copies)
	python3 /home/user01/Charles/Program/write_pdb.py
	cat Direction.pdb >> ../temp.pdb
	touch "$dir_fname"_.pdb
	mv ../temp.pdb ../"$dir_fname"_.pdb
	rm Direction.txt
	rm Direction.pdb
	#rm write_pdb.py
	cd ..
done
echo "Completed\n"
