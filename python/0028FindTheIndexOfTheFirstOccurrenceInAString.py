class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start

        return -1


class Solution:
    """
    time: O(n*m) == O(len(needle) * len(haystack) - len(needle))

    """

    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)

        for start in range(len(haystack)):
            end = start + length - 1

            # checked all possible options
            if end >= len(haystack):
                return -1

            if needle[-1] != haystack[end]:
                continue

            # check rest o' string
            if haystack[start : end + 1] == needle:
                return start

        return -1
