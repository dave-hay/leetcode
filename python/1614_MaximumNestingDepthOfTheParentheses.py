class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cur = 0

        for ch in s:
            if ch == "(":
                cur += 1
            elif ch == ")":
                cur -= 1

            res = max(res, cur)

        return res
