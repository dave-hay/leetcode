class Solution:
    """
    return true if pal
    or can u rm 1 char
    make it a list keep rming, have 1 pass
    """

    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(s):
            return s == s[::-1]

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Check if skipping either left or right leads to a palindrome
                return is_palindrome_range(
                    s[left + 1 : right + 1]
                ) or is_palindrome_range(s[left:right])
            left, right = left + 1, right - 1
        return True
