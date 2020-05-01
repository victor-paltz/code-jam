
def readline():
    return [int(x) for x in input().split()]


def max_bits(t, msp, R):
    bits_pos = [max(0, min(m, (t-p)//s)) for (m, s, p) in msp]
    bits_pos.sort(reverse=True)
    return sum(bits_pos[:R])


T = int(input())

for t in range(1, T+1):

    R, B, C = readline()

    msp = []
    for _ in range(C):
        msp.append(readline())

    t_left = 1
    t_right = int(1e20)

    while t_left != t_right:

        t_middle = t_left + (t_right-t_left)//2

        max_bit = max_bits(t_middle, msp, R)

        if max_bit >= B:
            t_right = min(t_middle, t_right-1)
        else:
            t_left = max(t_middle, t_left+1)

    print("Case #{}: {}".format(t, t_left))
