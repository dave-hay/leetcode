class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]

        def find(node):
            cur = node
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]

            return cur

        def union(n1, n2):
            par1, par2 = find(n1), find(n2)

            if par1 == par2:
                return False

            # par1 new parent
            if rank[par1] > rank[par2]:
                rank[par1] += rank[par2]
                parent[par2] = par1
            else:
                rank[par2] += rank[par1]
                parent[par1] = par2

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
