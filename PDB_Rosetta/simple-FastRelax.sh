#!/bin/bash

if [ $# -lt 2 ]; then
    echo "USAGE: simple-FastRelax.sh <input> <nstruct>"
    exit
fi
pdb=$1
nstruct=$2

/Users/iananderson/Downloads/rosetta_bin_mac_2021.16.61629_bundle/main/source/bin/rosetta_scripts.static.macosclangrelease \
-in:path:database /Users/iananderson/Downloads/rosetta_bin_mac_2021.16.61629_bundle/main/database \
-in:file:s ./$pdb \
-in:file:native ./$pdb \
-parser:protocol ./B_FastRelax.xml \
-relax:constrain_relax_to_start_coords \
-ignore_unrecognized_res \
-nstruct $nstruct \
-default_max_cycles 200 \
-out:prefix Fast-Relaxed- \
-out:file:silent ./Fast-Relax-$pdb.silent \
-out:file:silent_struct_type binary \
-out:file:scorefile ./Fast-Relax-$pdb.sc \
