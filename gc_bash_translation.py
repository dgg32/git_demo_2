#!/usr/bin/env bash
# input=$1

# aCount=$(grep -v ">" $input | grep -o "A" | wc -l)
# gCount=$(grep -v ">" $input | grep -o "G" | wc -l)
# cCount=$(grep -v ">" $input | grep -o "C" | wc -l)
# tCount=$(grep -v ">" $input | grep -o "T" | wc -l)
# nCount=$(grep -v ">" $input | grep -o "N" | wc -l)
# echo $(((cCount + gCount) * 100/(cCount + gCount + aCount + tCount + nCount)))

#!/usr/bin/env python 
import sys
input_file = sys.argv[1]

sequence = "".join([x for x in open(input_file).read().splitlines() if not x.startswith(">")])

aCount = sequence.count('A')
gCount = sequence.count('G')
cCount = sequence.count('C')
tCount = sequence.count('T')
nCount = sequence.count('N')

print (int((cCount + gCount) * 100/(aCount + gCount + cCount + tCount + nCount)))