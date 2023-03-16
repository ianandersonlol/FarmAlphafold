#!/bin/bash


/Users/iananderson/Downloads/rosetta_bin_mac_2021.16.61629_bundle/main/source/bin/docking_prepack_protocol.static.macosclangrelease \
-in:file:s Input/fixed_manihot_monomethyl_test.pdb \
-score:weights ref2015 \
-nstruct 10 \
-partners A_P \
-packing:pack_missing_sidechains 0 \
-chemical:include_patches lys_monomethylated \
-use_input_sc \
-docking:sc_min 1 \
-out:path:all prepack_output_files \
-out:suffix prepack

#-chemical:include_patches lys_monomethylated \
#-chemical:include_patches lys_dimethylated \
#-chemical:include_patches lys_trimethylated \

