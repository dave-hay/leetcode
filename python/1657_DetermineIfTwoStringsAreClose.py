class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2) or len(word1) != len(word2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(word1)):
            count1[ord(word1[i]) - ord("a")] += 1
            count2[ord(word2[i]) - ord("a")] += 1

        return sorted(count1) == sorted(count2)
