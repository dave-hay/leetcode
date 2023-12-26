class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def dp(memo, diceIndex, total):
            if memo[diceIndex][total] != -1:
                return memo[diceIndex][total]

            if diceIndex == n:
                if total == target:
                    return 1
                else:
                    return 0

            ways = 0
            end = min(k, target - total)
            for i in range(1, end + 1):
                ways = (ways + dp(memo, diceIndex + 1, total + i)) % (10**9 + 7)
            memo[diceIndex][total] = ways
            return memo[diceIndex][total]

        memo = [[-1] * (target + 1) for _ in range(n + 1)]
        res = dp(memo, 0, 0)
        return res
