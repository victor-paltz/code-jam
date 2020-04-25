import numpy as np
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


n = int(lines[0])
count = 1

for i in range(n):
    size = int(lines[count])
    count += 1
    m = [[int(x) for x in lin.split()] for lin in lines[count:count+size]]
    m = np.array(m)
    k = np.trace(m)
    r = sum(0 if len(set(x)) == size else 1 for x in m)
    c = sum(0 if len(set(x)) == size else 1 for x in m.T)
    print("Case #"+str(i+1)+": ", k, r, c)
    # print(m)
    count += size
