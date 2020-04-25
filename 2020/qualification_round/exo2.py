import numpy as np
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

n = lines[0]

for i, string in enumerate(lines[1:]):
    count = 0
    output = ""
    for c in string:
        val = int(c)
        if val >= count:
            output += "("*(val-count)
        else:
            output += ")"*(count-val)
        count = val
        output += c
    output += ")"*count
    print("Case #"+str(i+1)+": ", output)
