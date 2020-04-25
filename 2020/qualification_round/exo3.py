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
    data = [tuple([int(x) for x in lin.split()]+[ind])
            for ind, lin in enumerate(lines[count:count+size])]
    data.sort()
    count += size
    # print(data)

    sol = ["#"]*size
    J = 0
    C = 0

    for start, end, index in data:
        if start < J and start < C:
            print("Case #"+str(i+1)+": ", "IMPOSSIBLE")
            break
        elif start >= J and start < C:
            J = end
            sol[index] = "J"
        elif start < J and start >= C:
            C = end
            sol[index] = "C"
        else:
            if C < J:
                J = end
                sol[index] = "J"
            else:
                C = end
                sol[index] = "C"
    else:
        print("Case #"+str(i+1)+":", "".join(sol))
