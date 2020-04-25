
def readline_int_list():
    return [int(x) for x in input().split()]


def readline_chr():
    return input()


def readline_int():
    return int(input())


def solve(words):
    _, beg = max([(len(w), w) for w in words])
    for w in words:
        if not beg.startswith(w):
            return None
    return beg


T = readline_int()

for t in range(1, T+1):
    n = readline_int()
    words = [readline_chr() for _ in range(n)]

    beg_cons = [word.split("*")[0] for word in words]

    beg = solve(beg_cons)

    end_cons = [word.split("*")[-1][::-1] for word in words]

    end = solve(end_cons)

    if end is None or beg is None:
        sol = "*"
    else:
        end = end[::-1]

        sol = beg

        for w in words:
            sol += "".join(w.split("*")[1:-1])

        sol += end

    print("Case #{}: {}".format(t, sol))
