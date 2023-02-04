class Solution:
    """
    sliding window
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # track counts of s1
        s1map = [0] * 26
        s2map = [0] * 26
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord("a")] += 1
            s2map[ord(s2[i]) - ord("a")] += 1

        for i in range(len(s2) - len(s1)):
            if self.deepEquals(s1map, s2map):
                return True

            s2map[ord(s2[i + len(s1)]) - ord("a")] += 1
            s2map[ord(s2[i]) - ord("a")] -= 1

        return self.deepEquals(s1map, s2map)

    def deepEquals(self, mp1, mp2):
        for i in range(26):
            if mp1[i] != mp2[i]:
                return False
        return True


s = Solution()
res = s.checkInclusion("ab", "eidboaoo")
print(res)
# there are len(s2) // len(s1) options

res = s.checkInclusion("ab", "eidbaooo")
print(res)
