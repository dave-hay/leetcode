class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -(2**31), 2**31 - 1
        i = res = 0
        sign = "+"

        while i < len(s) and s[i].isspace():
            i += 1

        if i < len(s) and s[i] in "+-":
            sign = s[i]
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        if sign == "-":
            res *= -1

        if res < MIN:
            return MIN

        if res > MAX:
            return MAX

        return res
