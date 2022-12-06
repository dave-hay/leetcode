from functools import lru_cache


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
