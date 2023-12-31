class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = [0] * 26

        for w in words:
            for c in w:
                counts[ord(c) - ord("a")] += 1

        n = len(words)
        for val in counts:
            if val % n != 0:
                return False

        return True
