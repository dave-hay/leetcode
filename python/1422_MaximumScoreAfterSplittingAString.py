class OnePass:
    def maxScore(self, s: str) -> int:
        """
        time: O(n)
        space: O(1)
        """
        ones = 0
        zeros = 0
        best = float("-inf")

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1

            best = max(best, zeros - ones)

        if s[-1] == "1":
            ones += 1

        return best + ones


class TwoPass:
    def maxScore(self, s: str) -> int:
        """
        time: O(n)
        space: O(1)
        """
        ones = s.count("1")
        zeros = 0
        res = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            res = max(res, zeros + ones)
        return res
