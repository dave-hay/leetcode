class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for r in range(len(s) - 1, -1, -1):
            if s[r] == " ":
                continue
            l = r
            while l >= 0 and s[l] != " ":
                l -= 1

            return r - l
