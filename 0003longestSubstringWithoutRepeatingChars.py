class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if len(s) < 2:
            return len(s)

        seen = set()
        longest = 1
        cur = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                longest = max(cur, longest)

                while s[r] in seen:
                    seen.remove(s[l])
                    cur -= 1
                    l += 1

            seen.add(s[r])
            cur += 1

        return max(cur, longest)

    def lengthOfLongestSubstring2(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
