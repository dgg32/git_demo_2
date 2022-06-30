#!/usr/bin/env python 
import sys
input_file = sys.argv[1]

nucleotide_count = {"G": 0, "C": 0}

sequence = "".join([x for x in open(input_file).read().splitlines() if not x.startswith(">")])
num_nucleotide = len(sequence.replace("\n", ""))
for key in nucleotide_count:
    nucleotide_count[key] = sequence.count(key)

print (int((nucleotide_count["C"] + nucleotide_count["G"]) * 100/num_nucleotide))