class Solution:
    def tribonacci(self, n: int) -> int:
        seen = {1: 1, 2: 1}

        def trib(n):
            if n <= 0:
                return 0
            if n in seen:
                return seen[n]
            seen[n] = trib(n - 1) + trib(n - 2) + trib(n - 3)
            return seen[n]

        return trib(n)
