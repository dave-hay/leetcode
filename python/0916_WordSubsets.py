class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        b is subset of a, if every ch in b occurs in a
        a is universal if every string in words2 is a subset of a
        ----
        A: Brute force
            loop over words1 and for each words check against words2
            for each words1 check all words2
            words1 once and words2 n times
            time: O(n*m), space: o(1)

        B: keys
            create a map/array size 26 of chars of words2
            for each words1 do the same.
            where chars overlap make sure words2Array[i] >= words1Array[i]
        """
        get_ord = lambda ch: ord(ch) - ord("a")

        def create_key(word):
            key = [0] * 26

            for ch in word:
                key[get_ord(ch)] += 1

            return key

        res = []
        # create words2 key. use highest occurance of a char
        words2_key = [0] * 26
        for word in words2:
            # for each word create a key
            word_key = create_key(word)

            for i in range(26):
                words2_key[i] = max(words2_key[i], word_key[i])

        for word in words1:
            word_key = create_key(word)

            for i in range(26):
                if words2_key[i] > word_key[i]:
                    break

                if i == 25:
                    res.append(word)

        return res
