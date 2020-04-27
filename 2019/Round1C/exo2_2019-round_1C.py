
T, F = [int(x) for x in input().split()]

for t in range(1, T+1):

    remaining = set("ABCDE")
    letters = ""
    possibles = list(range(119))

    for rank in range(5):

        c = {x: [] for x in remaining}

        for n in possibles:
            print(n*5+rank+1, flush=True)
            letter = input()
            c[letter].append(n)

        _, letter, pos = min((len(pos), x, pos) for (x, pos) in c.items())

        possibles = pos
        letters += letter
        remaining.remove(letter)

    print(letters, flush=True)

    if input() == "N":
        exit()
