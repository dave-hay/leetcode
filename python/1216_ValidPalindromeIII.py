class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}

        def min_deletions(i, j):
            if i >= j:
                return 0
            if (i, j) not in memo:
                if s[i] == s[j]:
                    memo[(i, j)] = min_deletions(i + 1, j - 1)
                else:
                    memo[(i, j)] = 1 + min(
                        min_deletions(i + 1, j), min_deletions(i, j - 1)
                    )
            return memo[(i, j)]

        return min_deletions(0, len(s) - 1) <= k
