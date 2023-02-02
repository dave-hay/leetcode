class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True

        # build hashmap
        lang = {}
        for i in range(len(order)):
            lang[order[i]] = i

        def comp(w1, w2):
            if w1 == w2:
                return True
            length = min(len(w1), len(w2))
            for i in range(length):
                if lang[w1[i]] < lang[w2[i]]:
                    return True
                if lang[w1[i]] > lang[w2[i]]:
                    return False
            return len(w1) < len(w2)

        for i in range(len(words) - 1):
            if not comp(words[i], words[i + 1]):
                return False
        return True
