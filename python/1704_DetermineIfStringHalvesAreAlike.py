class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        slen = len(s)
        cur = 0

        for i in range(0, (slen // 2)):
            if s[i] in vowels:
                cur += 1

        for i in range((slen // 2), slen):
            if s[i] in vowels:
                cur -= 1

        return cur == 0
