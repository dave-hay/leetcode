from collections import deque


class Solution:

    def validPathBfs(self, n, edges, source, destination):
        """
        BFS variant
            Data Structures:
                Adjacency list
                Deque
                Set
            Algo:
                Pop deque from front(popleft)
                if val == destination valid path exists
                if already seen val then skip
                add all adjacent vertices to deque
                if all checked and not match then no path exists
        """
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        q = deque()
        q.append(source)
        seen = set()

        while q:
            cur = q.popleft()

            if cur == destination:
                return True

            if cur in seen:
                continue

            seen.add(cur)

            for node in adj[cur]:
                q.append(node)

        return False

    def validPathDfs(self, n: int, edges: list[list[int]], source: int,
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
