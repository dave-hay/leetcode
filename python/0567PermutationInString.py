class Solution:
    """
    sliding window
    n1, n2 = len(s1), len(s2)
    t: O(n1 + (n2 - n1))
    s: O(1)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # first window to match
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord("a")
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] + 1 == s2Count[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord("a")
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                matches -= 1
            l += 1
        return matches == 26


class Solution:
    """
    sliding window
    n1, n2 = len(s1), len(s2)
    t: O(n1 + 26(n2 - n1))
    s: O(1)
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
