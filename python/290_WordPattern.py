class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # should have same number of items
        if len(pattern) != len(words):
            return False

        # should have same number of unique items
        if len(set(pattern)) != len(set(words)):
            return False

        ch2word = {}

        # if mismatch will be found
        for i, ch in enumerate(pattern):
            word = words[i]

            if ch not in ch2word:
                ch2word[ch] = word
            elif ch2word[ch] != word:
                return False

        return True
