class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """
        diff[i][j] = 1R + 1C - 0R - 0C
        """
        ROWS, COLS = len(grid), len(grid[0])

        rows = {i: {0: 0, 1: 0} for i in range(ROWS)}
        cols = {i: {0: 0, 1: 0} for i in range(COLS)}

        # count number of 1 and zeros in col
        # dict?

        for r in range(ROWS):
            for c in range(COLS):
                val = grid[r][c]
                rows[r][val] += 1
                cols[c][val] += 1

        res = [[0] * (COLS) for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                res[r][c] = rows[r][1] + cols[c][1] - rows[r][0] - cols[c][0]

        return res
