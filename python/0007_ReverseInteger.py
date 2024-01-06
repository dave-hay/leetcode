class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = (-(2**31)), (2**31) - 1
        isNeg = False
        res = 0

        if x < 0:
            isNeg = True
            x *= -1

        while x:
            res = res * 10 + int(x % 10)
            x //= 10

        if isNeg:
            res *= -1

            return 0 if res < MIN else res

        return 0 if res > MAX else res
