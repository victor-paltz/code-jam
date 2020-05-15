
import sys

sys.setrecursionlimit(10000)


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


def winner(a, b):
    if a == b:
        return 0
    elif a == "P":
        return a if b == "R" else b
    elif a == "R":
        return a if b == "S" else b
    elif a == "S":
        return a if b == "P" else b
    else:
        raise


def ok_add(prev_list, new_move):

    if not prev_list:
        return True, [new_move]

    prev = prev_list[-1]

    if prev is None:
        return True, prev_list[:-1] + [new_move]
    if new_move == prev:
        return False, []
    else:
        w = winner(new_move, prev)
        ok, list_2 = ok_add(prev_list[:-1], w)

        return ok, list_2 + [None]


def solve(N, R, P, S):

    if R > P+S or P > R+S or S > P+R:
        return "IMPOSSIBLE"

    def aux(prev_list, R, P, S):
        if R+P+S == 0:
            return "-"

        # if R > P+S or P > R+S or S > P+R:
        #     return False

        for v in "PRS":
            if v == "P" and P <= 0:
                continue
            if v == "R" and R <= 0:
                continue
            if v == "S" and S <= 0:
                continue

            ok, new_list = ok_add(prev_list, v)

            if ok:
                test = aux(new_list, R - (1 if v == "R" else 0), P -
                           (1 if v == "P" else 0), S - (1 if v == "S" else 0))

                if test:
                    return v + test

        return False

    sol = aux([], R, P, S)

    # print(sol)

    if sol:
        return sol[:-1]

    return "IMPOSSIBLE"


T = readint()

for t in range(1, T+1):

    N, R, P, S = readints()

    print("Case #{}: {}".format(t, solve(N, R, P, S)))

    #print(ok_add(["P", "R", "P"], "S"))
