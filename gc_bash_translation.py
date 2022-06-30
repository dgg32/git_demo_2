
#!/usr/bin/env python 

def calculate_gc(sequence):
    aCount = sequence.count('A')
    gCount = sequence.count('G')
    cCount = sequence.count('C')
    tCount = sequence.count('T')
    nCount = sequence.count('N')

    return int((cCount + gCount) * 100/(aCount + gCount + cCount + tCount + nCount))

if __name__ == '__main__':
    import sys
    input_file = sys.argv[1]

    sequence = "".join([x for x in open(input_file).read().splitlines() if not x.startswith(">")])

    print (calculate_gc(sequence))