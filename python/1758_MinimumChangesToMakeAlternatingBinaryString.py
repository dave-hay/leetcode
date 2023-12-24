class Solution:
    """
    If it starts with 0 then every even index must be 0
    we will swap each time this is not true
    a string start with 1 will require the opposite number of swaps
    being len(s) - s0
    """

    def minOperations(self, s: str) -> int:
        s0 = 0

        for i, val in enumerate(s):
            if i % 2 == 0:
                if val == "1":
                    s0 += 1
            else:
                if val == "0":
                    s0 += 1

        return min(s0, len(s) - s0)
