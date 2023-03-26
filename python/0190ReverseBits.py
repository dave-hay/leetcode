class Solution:
    """
    32-bit mean binary string has indexes 0-31
    So to reverse we need to swap indexes: 0<=>31, 1<=>30, 2<=>29, etc.
    This is similar to (0 + i<=> 31 - i)

    1) create loop, 0 => 31
    2) get bit value from MSD to LSD (0 or 1)
    3) 'or' it to result in correct swapped  position
    """

    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # first bit put in 31, 1 in 30
            bit = (n >> i) & 1
            # start at largest
            res = res | (bit << (31 - i))
        return res
