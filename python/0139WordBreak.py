class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @cache
        def dp(indx):
            for i in range(indx, len(s)):
                if s[indx : i + 1] in words:
                    if i + 1 == len(s):
                        return True
                    if dp(i + 1):
                        return True

        return dp(0)
