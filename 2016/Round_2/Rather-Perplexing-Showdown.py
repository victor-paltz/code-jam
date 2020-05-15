
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for test in range(1, T+1):

    link = {}

    for v in "PRS":
        P, R, S = [1 if v == x else 0 for x in "PRS"]
        line = v
        for n in range(13):
            link[str(n)+"_"+str(P)+"_"+str(R)+"_"+str(S)] = line
            line = line.replace("P", "pr")
            line = line.replace("R", "rs")
            line = line.replace("S", "ps")
            line = line.upper()
            P, R, S = P+S, P+R, R+S

    N, R, P, S = readints()

    key = str(N)+"_"+str(P)+"_"+str(R)+"_"+str(S)

    if key not in link:
        print("Case #{}: IMPOSSIBLE".format(test))
        continue

    sol = list(link[key])

    for n in range(N):
        tmp = []
        for i in range(0, 2**(N-n), 2):
            tmp.append("".join(sorted(sol[i:i+2])))
        sol = tmp

    sol = "".join(sol)

    print("Case #{}: {}".format(test, sol))
