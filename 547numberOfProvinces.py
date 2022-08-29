class WQU:

    def __init__(self, size) -> None:
        self.id = list(range(size))
        self.sz = [1] * size
        self.size = size

    def find(self, x):
        """
        recursivly find root
        once found root is set to value of all children
        """
        if x == self.id[x]: return x
        self.id[x] = self.find(self.id[x])
        return self.id[x]

    def union(self, p, q):
        """
        set one equal to other
        """
        i = self.find(p)
        j = self.find(q)
        if i == j: return

        # assign the larger root to be the smallers new root
        # if equal replace root2's root with root1 + inc root1 size
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
        elif self.sz[i] > self.sz[j]:
            self.id[j] = i
        else:
            self.id[j] = i
            self.sz[i] += 1

        self.size -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        islands = len(isConnected)
        w = WQU(islands)

        for cur in range(islands):
            for con in range(islands):
                curIsland = isConnected[cur]
                connected = curIsland[con]

                if connected == 1:
                    w.union(cur, con)

        return w.size
