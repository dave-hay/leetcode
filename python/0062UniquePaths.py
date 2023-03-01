from collections import deque


class Solution:
    """
    row by row
    time: O(m x n) - every cell
    space: O(n) - row var re-used
    """

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]


class Solution:
    """
    BFS
    time: O(m x n) -  every node
    space: O(m x n) - create graph, set, q
    """

    def uniquePaths(self, m: int, n: int) -> int:
        # make a graph then traverse

        adj = [[0] * n for _ in range(m)]
        adj[m - 1][n - 1] = 1

        q = deque()
        seen = set()

        q.append((m - 1, n - 1))

        while q:
            cur = q.popleft()
            # if cur in seen do somethign
            if cur in seen:
                continue

            seen.add(cur)
            (row, col) = cur

            # go up?
            if row - 1 >= 0:
                q.append((row - 1, col))
            if col - 1 >= 0:
                q.append((row, col - 1))

            # check right
            if row + 1 < m:
                adj[row][col] += adj[row + 1][col]
            # check down
            if col + 1 < n:
                adj[row][col] += adj[row][col + 1]

        return adj[0][0]
