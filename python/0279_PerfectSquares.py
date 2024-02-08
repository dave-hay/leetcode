class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


class Solution:
    def numSquares(self, n: int) -> int:
        # map value: perfect squares needed
        mp = {0: 0, 1: 1}

        def dp(n):
            if n in mp:
                return mp[n]

            i = 1
            res = n
            while i * i <= n:
                res = min(res, dp(n - (i * i)) + 1)
                i += 1

            mp[n] = res
            return mp[n]

        return dp(n)
