class UF:
    def __init__(self, length):
        self.nums = [i for i in range(length)]
        self.weights = [1 for i in range(length)]
        self.groups = length

    def union(self, a, b):
        aPar = self.find(a)
        bPar = self.find(b)

        if aPar == bPar:
            return

        self.groups -= 1
        if self.weights[aPar] < self.weights[bPar]:
            self.nums[aPar] = bPar
        elif self.weights[aPar] > self.weights[bPar]:
            self.nums[bPar] = aPar
            pass
        else:
            self.nums[aPar] = bPar
            self.weights[aPar] += 1

    def find(self, a):
        if a != self.nums[a]:
            self.nums[a] = self.find(self.nums[a])

        return self.nums[a]


class Solution:
    """
    need comps - 1, cables len(connection)
    count connections len(connections[0])
    """

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UF(n)

        CONN = len(connections)

        for c in connections:
            uf.union(c[0], c[1])

        # already all connected
        if uf.groups == 1:
            return 0

        # not enough connections
        if CONN < n - 1:
            return -1

        # if fits dont need connect?
        return uf.groups - 1
