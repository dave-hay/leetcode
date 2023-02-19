class UF:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n

    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return False
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        # could do UF
        uf = UF(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        return True
