from itertools import cycle
from collections import Counter

T = int(input())

for t in range(1, T+1):
    n = int(input())
    words = [cycle(input()) for _ in range(n)]

    sucess = False
    sol = ""

    for i in range(500):
        letters = [next(x) for x in words]
        count = Counter(letters)

        if len(set(letters)) == 3:
            sucess = False
            break

        if count["P"] > 0 and count["S"] > 0:
            letter = "S"
        elif count["R"] > 0 and count["S"] > 0:
            letter = "R"
        elif count["R"] > 0 and count["P"] > 0:
            letter = "P"
        elif count["P"] > 0:
            letter = "S"
        elif count["S"] > 0:
            letter = "R"
        elif count["R"] > 0:
            letter = "P"

        sol += letter

        words = [c for first_letter, c in zip(
            letters, words) if first_letter == letter]

        if not words:
            sucess = True
            break

    if not sucess:
        print("Case #{}: IMPOSSIBLE".format(t))
    else:
        print("Case #{}: {}".format(t, sol))
