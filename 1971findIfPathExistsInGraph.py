class Solution:

    def validPath(self, n: int, edges: list[list[int]], source: int,
                  destination: int) -> bool:
        """
        DFS variant
            Data Structures:
                Adjacency list
                Stack
                Set
            Algo:
                Pop stack and if end return True
                else if already seen next loop
                else add popped to seen and add degrees to stack
        """
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        stack = [source]
        seen = set()

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            if node in seen:
                continue

            seen.add(node)

            for degree in adj[node]:
                stack.append(degree)

        return False
