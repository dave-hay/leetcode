class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0

        g.sort()
        s.sort()

        j = 0
        for i in range(len(s)):
            if j >= len(g):
                return j
            if s[i] >= g[j]:
                j += 1

        return j
