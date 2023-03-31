class Solution:
    """
    space/time: O(n)

    1. create arr dp of len n+1. dp[i] = i
    2. iterate with var i until n-3
    3. for each j from i + 3 to min(n, i+6) if greater dp[i] * (j - i - 1)
    4. return dp[n]
    """

    def maxA(self, n: int) -> int:
        # set up if just added one A each iter
        dp = list(range(n + 1))

        for i in range(n - 2):
            for j in range(i + 3, min(n, i + 6) + 1):
                dp[j] = max(dp[j], (j - i - 1) * dp[i])

        return dp[n]
