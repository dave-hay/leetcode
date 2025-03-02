class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = {}
        res = 0

        for ch in s:
            chars[ch] = chars.get(ch, 0) + 1
            if chars[ch] == 2:
                res += 2
                del chars[ch]

        if len(chars) > 0:
            res += 1

        return res
