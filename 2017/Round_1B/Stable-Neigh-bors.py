
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


T = readint()

for t in range(1, T+1):

    _ROYGBV = readints()
    _, R, O, Y, G, B, V = _ROYGBV

    if R == 0 and Y == 0 and G == 0 and V == 0:
        if B == O:
            print("Case #{}: {}".format(t, "BO"*B))
        else:
            print("Case #{}: IMPOSSIBLE".format(t))
        continue
    if B == 0 and Y == 0 and O == 0 and V == 0:
        if R == G:
            print("Case #{}: {}".format(t, "RG"*R))
        else:
            print("Case #{}: IMPOSSIBLE".format(t))
        continue
    if B == 0 and R == 0 and G == 0 and O == 0:
        if Y == V:
            print("Case #{}: {}".format(t, "YV"*Y))
        else:
            print("Case #{}: IMPOSSIBLE".format(t))
        continue

    if (O != 0 and O > B-1) or (G != 0 and G > R-1) or (V != 0 and V > Y-1):
        print("Case #{}: IMPOSSIBLE".format(t))
        continue

    B -= O
    R -= G
    Y -= V

    #print("BRY", B, R, Y)

    # if ROYGBV[4] !=  ROYGBV[2] or ROYGBV[4] !=  ROYGBV[2]

    data = [[count, letter] for letter, count in zip("BRY", [B, R, Y])]
    data.sort()
    # print(data)

    if data[2][0] > data[0][0] + data[1][0]:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue

    if data[1][0] - data[0][0] > data[2][0]:

        print("Case #{}: IMPOSSIBLE".format(t))
        continue

    output = [data[2][1] for _ in range(data[2][0])]

    ok = True
    i = 0
    while data[0][0] > 0 or data[1][0] > 0:
        if output[i][-1] != data[1][1] and data[1][0] > 0:
            output[i] += data[1][1]
            data[1][0] -= 1
        elif output[i][-1] != data[0][1] and data[0][0] > 0:
            output[i] += data[0][1]
            data[0][0] -= 1
        else:
            ok = False
            break
        i = (i+1) % data[2][0]

    if not ok:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue

    true_sol = "".join(output)

    #print(output, O, G, V)

    if O > 0:
        index = true_sol.index("B")
        true_sol = true_sol[:index] + "BO"*O + true_sol[index:]
    if G > 0:
        index = true_sol.index("R")
        true_sol = true_sol[:index] + "RG"*G + true_sol[index:]
    if V > 0:
        index = true_sol.index("Y")
        true_sol = true_sol[:index] + "YV"*V + true_sol[index:]

    print("Case #{}: {}".format(t, true_sol))
