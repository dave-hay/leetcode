class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1] * (n + 1)

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]


class Solution:
    def climbStairs(self, n: int, cache={0: 1}) -> int:
        if n in cache:
            return cache[n]
        if n < 0:
            return 0

        cache[n - 1] = self.climbStairs(n - 1)
        cache[n - 2] = self.climbStairs(n - 2)

        return cache[n - 1] + cache[n - 2]
