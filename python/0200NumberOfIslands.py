from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        seen = set()

        # replace with hash
        def bfs(r, c):
            d = deque()
            seen.add((r, c))
            d.append((r, c))
            while d:
                curRow, curCol = d.popleft()  # changing to pop() will make it dfs
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    row, col = curRow + dr, curCol + dc
                    if (
                        row in range(ROWS)
                        and col in range(COLS)
                        and grid[row][col] == "1"
                        and (row, col) not in seen
                    ):
                        d.append((row, col))
                        seen.add((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    # run traversal
                    bfs(r, c)
                    res += 1

        return res
