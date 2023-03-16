#!/bin/bash
#$ -S /bin/bash

#SBATCH --array=1-1000
#SBATCH --job-name=di-refinement_docking
#SBATCH --time=1-0
#SBATCH --partition=bmh
#SBATCH --mail-user=dpquiroz@ucdavis.edu
#SBATCH --mail-type=ALL

/home/dpquiroz/Applications/rosetta_bin_linux_2021.16.61629_bundle/main/source/bin/docking_protocol.static.linuxgccrelease \
-database /home/dpquiroz/Applications/rosetta_bin_linux_2021.16.61629_bundle/main/database \
-in:file:s Inputs/H3K4di_Tudor_relaxed_AP.pdb \
-in:file:native ./7de9_AP.pdb \
-score:weights ref2015 \
-nstruct 10 \
-partners A_P \
-docking:sc_min 1 \
-packing:pack_missing_sidechains 0 \
-chemical:include_patches lys_dimethylated \
-docking_local_refine \
-use_input_sc \
-ex1 \
-ex2 \
-ex3 \
-ex4 \
-ex1aro \
-ex2aro \
-out:suffix _refinement_dock \
-out:file:scorefile ./docking_output_files/H3K4di_Tudor_relaxed_AP_refinement-T2.sc \
-out:file:silent ./docking_output_files/H3K4di_Tudor_relaxed_AP_refinement-${SLURM_ARRAY_TASK_ID}.silent \
-out:file:silent_struct_type binary \
-out:file:fullatom \
-score:docking_interface_score 1 \
-mute all
