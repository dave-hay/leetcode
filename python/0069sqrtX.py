class Solution:
    """
    Time Complexity: O(log N)
        Binary search always O(log N)
    Space Complexity: O(1)

    Notes:
        If sqrt(x) == whole number:
            The while loop will be able to match exactly as guesses are truncated.
            Ex. x=4 sqrt=2

        If sqrt(x) == real number:
            - Loop will eventually exit as no match possible.
            - When loop exits sqrt(x) will be somewhere between lo and hi.
            - Since loop incr by one and exits when lo is greater we know
                lo = hi + 1 as the loop beforehand lo == hi
            - That means lo is the ceil and hi is the floor.
                hi(floor) < sqrt(x) < lo(ceil)
            - As they're both while numbers sqrt(x) is going to be hi.[some nums]
            - return hi
    """

    def mySqrt(self, x: int) -> int:
        # first if 0 or 1 return self
        if x < 2:
            return x

        # binary search
        # lo = 2 since 0 and 1 are out of picture
        lo = 2

        # hi = x // 2  root of x is always smaller than half
        hi = x // 2

        while lo <= hi:
            mid = (lo + hi) // 2
            guess = mid * mid

            if guess > x:
                hi = mid - 1
            elif guess < x:
                lo = mid + 1
            else:
                return mid

        # if loop breaks return floor
        return hi
