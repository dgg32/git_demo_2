#!/usr/bin/env python 
from Bio.SeqUtils import GC
import sys
input_file = sys.argv[1]

sequence = "".join([x for x in open(input_file).read().splitlines() if not x.startswith(">")])
print(GC(sequence))