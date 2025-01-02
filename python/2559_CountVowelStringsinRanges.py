class Solution:
    """
    n = words, m = queries
    time: o(n + m)
    space: o(n)
    """

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(["a", "e", "i", "o", "u"])
        pre = [0] * (len(words) + 1)
        res = []

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                pre[i + 1] = pre[i] + 1
            else:
                pre[i + 1] = pre[i]

        for l, r in queries:
            res.append(pre[r + 1] - pre[l])

        return res
