class Solution:
    """
    Pop Count
    t: O(n * log n)
    s: O(1)
    """

    def countBits(self, n: int) -> List[int]:
        def bits(n, count):
            if n == 0:
                return count
            n &= n - 1
            return bits(n, count + 1)

        res = []
        for i in range(n + 1):
            res.append(bits(i, 0))

        return res
