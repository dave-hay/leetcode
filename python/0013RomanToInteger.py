class Solution:
    def romanToInt(self, s: str) -> int:
        Map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # if a lower val is before larger subtract else add
        res = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and Map[s[i]] < Map[s[i + 1]]:
                res += Map[s[i + 1]] - Map[s[i]]
                i += 2
            else:
                res += Map[s[i]]
                i += 1
        return res
