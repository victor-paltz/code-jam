import numpy as np


def area_sum(a2, i1, i2, j1, j2):

    #n, m = a2.shape()

    if j2 <= j1 or i2 <= i1:
        return 0

    res = a2[i2-1][j2-1]

    if i1 > 0:
        res -= a2[i1-1][j2-1]

    if j1 > 0:
        res -= a2[i2-1][j1-1]

    if i1 > 0 and j1 > 0:
        res += a2[i1-1][j1-1]

    return res


def del_empty_lines(m):
    m2 = []
    for x in m:
        if np.any(x):
            m2.append(x)
    return np.array(m2)


def del_empty_cols(m):
    return del_empty_lines(m.T).T


def solve(h_list, v_list, h, v, n, m, qte):

    #print(h_list, v_list, h, v, n, m, qte)

    h_prev, v_prev = h_list[-1], v_list[-1]

    h_test = list(range(h_list[-1]+1, n+1))
    v_test = list(range(v_list[-1]+1, m+1))

    if h_prev == n and v_prev == m:
        return True

    if h == 0 and h_prev != n:
        h += 1
        h_test = [n]

    if v == 0 and v_prev != m:
        v += 1
        v_test = [m]

    if h_test and v_test:
        for h_cut in h_test:
            for v_cut in v_test:

                choc = area_sum(mat2, h_prev, h_cut, v_prev, v_cut)

                if choc > qte:
                    break

                if choc == qte:
                    if area_sum(mat2, 0, n, v_prev, v_cut) == qte*(H+1):
                        if area_sum(mat2, h_prev, h_cut, 0, m) == qte*(V+1):
                            ok = True

                            for (h1, h2) in zip(h_list, h_list[1:]):
                                if area_sum(mat2, h1, h2, v_prev, v_cut) != qte:
                                    ok = False
                                    break
                            if ok:
                                for (v1, v2) in zip(v_list, v_list[1:]):
                                    if area_sum(mat2, h_prev, h_cut, v1, v2) != qte:
                                        ok = False
                                        break
                                if ok:
                                    if solve(h_list+[h_cut], v_list+[v_cut], h-1, v-1, n, m, qte):
                                        return True
    elif h_test:

        for h_cut in h_test:

            if area_sum(mat2, h_prev, h_cut, 0, m) > qte*(V+1):
                return False

            if area_sum(mat2, h_prev, h_cut, 0, m) == qte*(V+1):

                for (v1, v2) in zip(v_list, v_list[1:]):
                    if area_sum(mat2, h_prev, h_cut, v1, v2) > qte:
                        return False

                ok = True
                for (v1, v2) in zip(v_list, v_list[1:]):
                    if area_sum(mat2, h_prev, h_cut, v1, v2) != qte:
                        ok = False
                        break

                if ok:
                    if solve(h_list+[h_cut], v_list, h-1, v, n, m, qte):
                        return True

    elif v_test:

        for v_cut in v_test:

            if area_sum(mat2, 0, n, v_prev, v_cut) > qte*(H+1):
                return False

            if area_sum(mat2, 0, n, v_prev, v_cut) == qte*(H+1):

                for (h1, h2) in zip(h_list, h_list[1:]):
                    if area_sum(mat2, h1, h2, v_prev, v_cut) > qte:
                        return False

                ok = True
                for (v1, v2) in zip(v_list, v_list[1:]):
                    if area_sum(mat2, h1, h2, v_prev, v_cut) != qte:
                        ok = False
                        break

                if ok:
                    if solve(h_list, v_list+[v_cut], h, v-1, n, m, qte):
                        return True

    return False


T = int(input())

for t in range(1, T+1):

    R, C, H, V = [int(x) for x in input().split(" ")]

    mat = []
    for _ in range(R):
        mat.append([1 if x == "@" else 0 for x in input()])
    mat = np.array(mat)

    if np.sum(mat) == 0:
        print("Case #{}: POSSIBLE".format(t))
        continue

    mat = del_empty_lines(del_empty_cols(mat))
    n, m = mat.shape

    mat2 = np.cumsum(np.cumsum(mat, axis=1), axis=0)

    tot = (H+1)*(V+1)

    if np.sum(mat) % tot:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue

    qte = np.sum(mat)//tot

    # print(mat)

    if solve([0], [0], H, V, n, m, qte):
        print("Case #{}: POSSIBLE".format(t))
    else:
        print("Case #{}: IMPOSSIBLE".format(t))
