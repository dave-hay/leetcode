class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        number of islands but max length
        iterate over each cell
        skip if 0
        dfs if 1
        replace 1 with 0
        when over update max size
        """
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maxArea = 0

        def dfs(row, col):
            s = [(row, col)]
            area = 0

            while s:
                r, c = s.pop()

                # check if in bounds
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                    continue

                area += 1
                grid[r][c] = 0

                for dr, dc in DIRS:
                    nr, nc = dr + r, dc + c
                    s.append((nr, nc))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
