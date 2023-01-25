"""
time - O(n^2)
space - O(1)
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            left, right = i, i
            while (
                left <= right and right < len(s) and left >= 0 and s[left] == s[right]
            ):
                res += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            left, right = i, i + 1
            while (
                left <= right and right < len(s) and left >= 0 and s[left] == s[right]
            ):
                res += 1
                left -= 1
                right += 1

        return res
