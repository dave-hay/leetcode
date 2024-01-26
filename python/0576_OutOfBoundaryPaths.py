class Solution:
    """
    time + space: O(m * n * maxMoves)
    """

    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        MOD = 10**9 + 7
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dp = [[[-1 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]

        def backtrack(r, c, moves):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 1

            if moves == 0:
                return 0

            if dp[r][c][moves] != -1:
                return dp[r][c][moves]

            res = 0
            for dr, dc in DIRS:
                res += backtrack(r + dr, c + dc, moves - 1)

            dp[r][c][moves] = res
            return res % MOD

        return backtrack(startRow, startColumn, maxMove)
