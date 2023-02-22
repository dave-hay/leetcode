from functools import lru_cache


class Solution:
    """
    iterative approach
    time: O(amount * len(coins))
    space: O(amount)
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        if coins[0] > amount:
            return -1
        # other option is to check with division or bottom up

        @lru_cache(None)
        def dfs(total):
            if total < 0:
                return -1
            if total == 0:
                return 0

            minCoins = float("inf")

            for coin in coins:
                res = dfs(total - coin)
                if res != -1:
                    minCoins = min(minCoins, res + 1)
            return minCoins if minCoins != float("inf") else -1

        return dfs(amount)
