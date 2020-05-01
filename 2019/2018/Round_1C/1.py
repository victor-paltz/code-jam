from collections import Counter


def readline():
    return [int(x) for x in input().split()]


T = int(input())

for t in range(1, T+1):
    N, L = readline()

    words = []
    for _ in range(N):
        words.append(list(input()))

    words.sort()

    pos_letters = [set(w[i] for w in words) for i in range(L)]
    # print(pos_letters)
    diff = [len(set(w[i] for w in words)) for i in range(L)]

    def solution(curr_words, i, n):
        if i == n:
            return "-"

        c = Counter(w[0] for w in curr_words)

        mini, letter = float("inf"), ""
        for x in pos_letters[i]:
            if c[x] < mini:
                mini = c[x]
                letter = x

        if c[letter] == 0:
            return letter+"".join(x.pop() for x in pos_letters[i+1:])

        new_words = [w[1:] for w in curr_words if w[0] == letter]

        return letter + solution(new_words, i+1, n)

    s = solution(words, 0, L)

    if s[-1] == "-":
        s = "-"

    print("Case #{}: {}".format(t, s))
