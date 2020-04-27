
from collections import defaultdict


class Trie:

    def __init__(self, words=None):
        self.data = 0
        self.sons = defaultdict(Trie)

        if words:
            for w in words:
                self.add(w)

    def add(self, word):
        if word:
            prefix, *suffix = word
            self.sons[prefix].add(suffix)
        else:
            self.data += 1

    def __delitem__(self, key):
        del self.sons[key]

    def __getitem__(self, key):
        return self.sons[key]

    def __setitem__(self, key, value):
        self.sons[key] = value

    def __repr__(self):
        return str((dict(self.sons), self.data))


def f(trie):
    r = sum(f(v) for v in trie.sons.values())
    r += trie.data
    if r >= 2:
        r -= 2
    return r


T = int(input())

for t in range(1, T+1):

    n = int(input())
    words = [input() for _ in range(n)]

    trie = Trie()

    for w in words:
        trie.add(w[::-1])

    val = sum(f(v) for v in trie.sons.values()) + trie.data

    print("Case #{}: {}".format(t, len(words)-val))
