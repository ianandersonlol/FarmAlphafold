import os
import Bio
from Bio.PDB import PDBParser, PDBIO, Superimposer


    
def align(structure1):
    base_name = os.path.splitext(os.path.basename(structure1))[0]
    # Create a list of the atoms in each structure
    structure3 = PDBParser().get_structure('sample', structure1)
    structure2 = PDBParser().get_structure('reference', 'tudoralign.pdb')
    
    atoms1 = Bio.PDB.Selection.unfold_entities(structure3, 'A')
    num_atoms1 = len(atoms1)
    print("Hello")
    atoms2 = Bio.PDB.Selection.unfold_entities(structure2, 'A')
    num_atoms2 = len(atoms2)
    print("This sucks")
    num_atoms = min(num_atoms1, num_atoms2)
    print("Aligning across..."+str(num_atoms)+" atoms")
    atoms1 = atoms1[:num_atoms]
    atoms2 = atoms2[:num_atoms]
    # Create a superimposer object
    superimposer = Bio.PDB.Superimposer()

    # Align the structures
    superimposer.set_atoms(atoms1, atoms2)
    superimposer.apply(atoms2)

    # Write the aligned structure to a new PDB file
    io = Bio.PDB.PDBIO()
    io.set_structure(structure3)
    io.save(base_name+'_aligned.pdb')
    # open the two PDB files
    with open(base_name+'_aligned.pdb', 'r') as f1, open('dimethylation.pdb', 'r') as f2:
        # read the lines from each file
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # combine the lines from both files into a single list
    combined_lines = lines1 + lines2

    # write the combined lines to a new PDB file
    with open(base_name+'_dimethyl.pdb', 'w') as f:
        f.writelines(combined_lines)
        
if __name__ == '__main__':
    import sys
    if not sys.argv[1]:
        exit()
    align(sys.argv[1])