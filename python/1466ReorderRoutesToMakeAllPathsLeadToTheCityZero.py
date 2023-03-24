class Solution:
    """
    s: O(n)
    t: O(n)
    """

    def __init__(self) -> None:
        self.count = 0

    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]

        for c in connections:
            adj[c[0]].append((c[1], 1))  # origional edge
            adj[c[1]].append((c[0], 0))  # artificial edge

        def dfs(node, parent, adj):
            for child, sign in adj[node]:
                if child != parent:
                    self.count += sign
                    dfs(child, node, adj)

        dfs(0, -1, adj)
        return self.count
