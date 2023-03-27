class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # dfs
        def dfs(r, c):
            res = grid[r][c]

            if c == COLS - 1 and r == ROWS - 1:
                return res

            # at last row
            if c < COLS - 1 and r == ROWS - 1:
                return dfs(r, c + 1) + res

            # at last col
            if c == COLS - 1 and r < ROWS - 1:
                return dfs(r + 1, c) + res

            return res + min(dfs(r, c + 1), dfs(r + 1, c))

        return dfs(0, 0)
