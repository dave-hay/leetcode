class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # save index farthest left
        mp = {}  # char: index first occurance of char
        res = -1
        for i, c in enumerate(s):
            if c in mp:
                res = max(res, i - mp[c] - 1)
            else:
                mp[c] = i

        return res
