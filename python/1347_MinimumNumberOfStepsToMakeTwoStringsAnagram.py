class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = [0] * 26

        for i in range(len(s)):
            res[ord(s[i]) - ord("a")] += 1
            res[ord(t[i]) - ord("a")] -= 1

        ans = 0
        for i in res:
            if i > 0:
                ans += i

        return ans
