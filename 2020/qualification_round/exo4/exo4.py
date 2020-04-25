
def readline_int_list():
    return [int(x) for x in input().split()]


def readline_chr():
    return input()


def readline_int():
    return int(input())


NOT_FOUND = -10

T, B = readline_int_list()

for t in range(T):

    tab = [NOT_FOUND]*B
    coup = 1

    while (NOT_FOUND in tab) or (coup % 10 == 1):

        if coup % 10 == 1 and coup != 1:

            toggle = [1-x if x in [0, 1] else x for x in tab]
            possible = [tab, list(reversed(tab)), toggle,
                        list(reversed(toggle))]
            possible = set(tuple(x) for x in possible)
            possible = [list(x) for x in possible]

            i = 0
            while (len(possible) > 1) or (i == 0):  # must be done at least once

                if i >= B:
                    i = 0
                    while len(possible) > 1:
                        # exit()
                        try:
                            assert i < B
                        except:
                            i = 0
                            #raise ValueError(str(possible))
                        if len(set(x[i] for x in possible)) > 1:
                            print(i+1, flush=True)
                            coup += 1
                            val = readline_int()
                            possible = [x for x in possible if x[i]
                                        == val or x[i] == NOT_FOUND]
                            for k in range(len(possible)):
                                possible[k][i] = val

                            possible = set(tuple(x) for x in possible)
                            possible = [list(x) for x in possible]
                        i += 1
                    continue

                if len(set(x[i] for x in possible).difference(set([NOT_FOUND]))) > 1:
                    print(i+1, flush=True)
                    coup += 1
                    val = readline_int()
                    possible = [x for x in possible if x[i] == val]
                i += 1

            assert len(possible) == 1

            tab = possible[0]

            continue

        # tant pis pour la complexité quadratique, on pourrait mieux faire
        index_left = tab.index(NOT_FOUND)
        opp_index_right = list(reversed(tab)).index(NOT_FOUND)

        if index_left <= opp_index_right:
            print(index_left+1, flush=True)
            coup += 1
            tab[index_left] = readline_int()
            continue
        else:
            print(B-opp_index_right, flush=True)
            coup += 1
            tab[B-opp_index_right-1] = readline_int()
            continue

    if NOT_FOUND not in tab:
        print("".join(str(x) for x in tab), flush=True)
        ok = readline_chr()
        if ok == "N":
            exit()
