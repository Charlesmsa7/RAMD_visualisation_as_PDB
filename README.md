# RAMD_visualisation_as_PDB
Short description: This script will helpt to visualize RAMD results in protein 3D structures. 

In Brief: RAMD (Random Acceleration Molecular Dynamics) simulations will provide possible ligand dissociation paths.
Visualizing the paths are usually mentioned as "the path between Helix1 and Helix4".

But, difficult to depict visually using conventional visualizing programs.

This tool extract the COM (Centre of Mass) of Ligand at every written record (silumation .log/.out file)
and creates the COM as Dummy atom. And at the dissociation path will be added as ligand molecule with hetero atoms.

The the final structurs can be easily visualized using any of the tools such as PyMol, chimera, etc.,

Go through the scripts for clear understaning, 

This amature script can be easily modified accoding to the users need/system enviroiment.
