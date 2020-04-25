import numpy as np


def readline_int_list():
    return [int(x) for x in input().split()]


def readline_chr():
    return input()


def readline_int():
    return int(input())


def distinct(tab):
    return len(list(set(tab))) == len(tab)


def dumb_latin(values):
    n = len(values)
    mat = np.zeros((n, n))
    for i, val in enumerate(values):
        mat += np.diag([val]*(i+1), i-n+1)
    for i, val in enumerate(values[:-1]):
        mat += np.diag([val]*(n-i-1), i+1)
    return mat.astype(np.uint8)


def fill(mat, n):
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                for k in range(1, n+1):
                    if k not in mat[i] and k not in mat[:, j]:
                        mat[i][j] = k
                        c, res = fill(mat, n)
                        if c:
                            return c, res
                mat[i][j] = 0
                return False, None
    return True, mat


def get_a_b_c(N, K):
    if K % N == 0:
        v = K//N
        return (v, v, v)

    b = c = -1
    for a in range(1, min(K//(N-2), N)+1):
        r = K - a*(N-2)
        if r >= 2*N:
            continue
        else:
            for i in range(max(1, r-N), min(r, N+1)):
                b = i
                c = r-i
                if distinct([a, b]) and distinct([a, c]):
                    if N == 3:
                        if distinct([b, c]):
                            break
                    else:
                        break

        if a*(N-2)+b+c == K and a != b and a != c:
            if N == 3:
                if distinct([b, c]):
                    break
            else:
                break

    if a*(N-2)+b+c != K or (len(set([a, b, c])) == 2 and N == 3):
        # print(N, K)
        return (-1, -1, -1)

    assert 1 <= a <= N and 1 <= b <= N and 1 <= c <= N
    assert a*(N-2)+b+c == K and distinct([a, b]) and distinct([a, c])

    return (a, b, c)


def format_output(mat):
    for lin in mat:
        print(" ".join([str(x) for x in lin]))


T = readline_int()

for t in range(T):

    N, K = readline_int_list()

    if N+1 == K or N*N-1 == K:
        print("Case #"+str(t+1)+": IMPOSSIBLE")
        continue

    mat = np.zeros((N, N), dtype=int)

    if N == 2:
        print("Case #"+str(t+1)+": POSSIBLE")
        if K == 2:
            mat = np.array([[1, 2], [2, 1]])
        else:
            mat = np.array([[2, 1], [1, 2]])

    elif K % N == 0:
        print("Case #"+str(t+1)+": POSSIBLE")
        v = K//N
        diag = [i for i in range(1, N+1) if i != v]
        diag.append(v)
        mat = dumb_latin(diag)
    else:
        a, b, c = get_a_b_c(N, K)

        if a == -1 or b == -1 or c == -1:
            print("Case #"+str(t+1)+": IMPOSSIBLE")
            continue

        print("Case #"+str(t+1)+": POSSIBLE")
        if N <= 5:
            diag = [a]*(N-2)+[b, c]
            ok, mat = fill(np.diag(diag), len(diag))
            if not ok:
                print(N, K)
                print(a, b, c)
                print(diag)
                exit()
        else:

            def rec(a, b, c, n):
                if n % 2 == 0:
                    l1 = []
                    i = 1
                    while len(l1) < n//2-3:
                        if i != a and i != b and i != c:
                            l1.append(i)
                    l1.append(a)

                    mat[:n//2, :n//2] = dumb_latin(l1)

    format_output(mat)
