class Solution:
    """
    n & n-1 will always flip the least significant 1-bit to 0
    """

    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += 1
            n &= n - 1
        return count
