class Solution:
    """
    for a unique palindrome of len(3)
        only first and last chars matter
        middle can be any char
    ---
    want to find the biggest range between matching chars
    - it will contain all palindromes that could be created in substrings

    time: o(n)
    space: o(1) chars are 26 max
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        res = 0

        for letter in letters:
            l, r = s.index(letter), s.rindex(letter)
            res += len(set(s[l + 1 : r]))

        return res
