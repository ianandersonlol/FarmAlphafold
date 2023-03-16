#!/bin/bash

silent=$1
tag=$2
if [ $# -lt 2 ]; then
    echo "USAGE: extract-pdbs.sh <silent-file> <tag>"
    exit
fi

mkdir pdbs1
cd pdbs1

/Users/iananderson/Downloads/rosetta_bin_mac_2021.16.61629_bundle/main/source/bin/score_jd2.static.macosclangrelease \
-in:file:fullatom \
-in:file:silent ../$silent \
-in:file:silent_struct_type binary \
-in::missing_density_to_jump \
-in::use_truncated_termini \
-in:file:tags $2 \
-ignore_unrecognized_res \
-out:pdb \
-out:prefix score- \
-overwrite \