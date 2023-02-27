class Solution:
    """
    DP Iterative
    time/space: O(n)/O(n)
    """

    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i < len(s) - 1 and (s[i] == "2" and s[i + 1] < "7" or s[i] == "1"):
                dp[i] += dp[i + 2]

        return dp[0]


class Solution:
    """
    DP Recursive
    time/space: O(n)/O(n)
    """

    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0

            cur = dp(i + 1)

            if i < len(s) - 1 and (s[i] == "2" and s[i + 1] < "7" or s[i] == "1"):
                cur += dp(i + 2)

            return cur

        return dp(0)
