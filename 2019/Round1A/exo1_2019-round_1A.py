
T = int(input())

for t in range(1, T+1):

    row, col = [int(x) for x in input().split()]

    if row < 5 and col < 5 and (row, col) not in [(3, 4), (4, 3), (4, 4)]:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue
    else:
        print("Case #{}: POSSIBLE".format(t))

        rev = False

        if col < 5 and row != 3:
            row, col = col, row
            rev = True

    data = []

    if (row, col) == (4, 4):

        for j in [0, 3, 2, 1]:
            for i in range(4):
                data.append((i, (j+1 + (1 if i % 2 else -1) + 4) % 4))
    else:

        x, y = 0, 0

        if row % 2:
            x, y = 1, 0
            for _ in range(col):
                data.append((x % col, y))
                data.append(((x+1) % col, y+2))
                data.append(((x+3) % col, y+1))
                x += 1
            y += 3

        x = 0
        for _ in range((row-y)//2):
            for _ in range(col):
                data.append((x % col, y))
                data.append(((x+3) % col, y+1))
                x += 1
            y += 2

        if rev:
            row, col = col, row
            data = [(y, x) for (x, y) in data]

    for x, y in data:
        print(y+1, x+1)

    # Test part
    assert len(set(data)) == row*col
    for (x1, y1), (x2, y2) in zip(data, data[1:]):
        assert x1 != x2
        assert y1 != y2
        if x1-y1 == x2-y2:
            print((x1, y1), (x2, y2))
        if x1+y1 == x2+y2:
            print((x1, y1), (x2, y2))
        assert x1-y1 != x2-y2
        assert x1+y1 != x2+y2

    for (x1, y1) in data:
        assert 0 <= x1 <= col
        assert 0 <= y1 <= row
