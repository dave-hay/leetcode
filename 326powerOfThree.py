class Solution:

    def isPowerOfThree(self, n):
        if n == 1: return True
        if n == 0: return False
        # if real number
        if n / 3 == float(int(n / 3)) or n == 1:
            num = n / 3
            return self.isPowerOfThree(num)
        else:
            return False
