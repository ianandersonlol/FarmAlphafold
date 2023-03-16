#!/bin/bash

silent=$1
if [ $# -lt 1 ]; then
    echo "USAGE: extract-pdbs.sh <silent-file> "
    exit
fi

mkdir pdbs
cd pdbs

/Users/iananderson/Downloads/rosetta_bin_mac_2021.16.61629_bundle/main/source/bin/score_jd2.static.macosclangrelease \
-in:file:fullatom \
-in:file:silent ../$silent \
-in:file:silent_struct_type binary \
-in::missing_density_to_jump \
-in::use_truncated_termini \
-ignore_unrecognized_res \
-out:pdb \
-out:prefix score- \
-out:file:scorefile score-file.sc \