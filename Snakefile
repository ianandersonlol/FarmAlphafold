import os

input_pdb = config["input_pdb"]

rule all:
    input:
        "final_output/flexpepdock_output.pdb"

rule fastrelax:
    output:
        temp("fastrelax_output/{num}.pdb")
    shell:
        "rosetta_scripts.linuxgccrelease -parser:protocol fastrelax.xml -s {input_pdb} -nstruct 500 -out:pdb_gz -out:file:silent_struct_type binary -out:file:scorefile score.sc -out:prefix fastrelax_output/ -suffix _{wildcards.num}"

rule extract_best:
    input:
        scores="score.sc",
        fastrelax_output=expand("fastrelax_output/{num}.pdb", num=range(1, 501))
    output:
        "best_pdb.pdb"
    run:
        best_score = float("inf")
        best_file = ""
        with open(input.scores, "r") as f:
            next(f)  # Skip header
            for line in f:
                fields = line.split()
                score = float(fields[1])
                pdb_file = fields[-1]
                if score < best_score:
                    best_score = score
                    best_file = pdb_file
        os.system(f"cp {best_file} {output}")

rule clean_pdb:
    input:
        "best_pdb.pdb"
    output:
        "cleaned_pdb.pdb"
    shell:
        "rosetta_scripts.linuxgccrelease -parser:protocol cleanPDB.xml -s {input} -out:file:o {output}"

rule merge_pdbs:
    input:
        pdb1="cleaned_pdb.pdb",
        pdb2="/home/icanders/setpdbs/h3k4me1.pdb"
    output:
        "merged_pdb.pdb"
    shell:
        "chimerax --headless --nogui --script 'open {input.pdb1}; open {input.pdb2}; save {output}'"

rule superimpose:
    input:
        merged_pdb="merged_pdb.pdb",
        anchor_pdb="/home/icanders/setpdbs/anchor.pdb"
    output:
        "superimposed_pdb.pdb"
    shell:
        "chimerax --headless --nogui --script 'open {input.merged_pdb}; open {input.anchor_pdb}; mm #1 #2; save {output} #1'"

rule flexpepdock:
    input:
        "superimposed_pdb.pdb"
    output:
        "final_output/flexpepdock_output.pdb"
    shell:
        "rosetta_scripts.linuxgccrelease -parser:protocol flexpepdock.xml -s {input} -nstruct 10000 -out:prefix final_output/ -out:file:o {output}"
