class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            cur = s[l]
            # while current left == next iterate
            while l <= r and s[l] == cur:
                l += 1

            # while current right == prev iterate
            while l < r and s[r] == cur:
                r -= 1

        return r - l + 1


class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            cur = s[l]

            # while current left == next iterate
            while l < r and s[l] == cur:
                l += 1

            if l == r:
                return 0

            # while current left == next iterate
            while l < r and s[r] == cur:
                r -= 1

        return r - l + 1


class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            # while current left == next iterate
            while l < r and s[l] == s[l + 1]:
                l += 1

            # while current left == next iterate
            while l < r and s[r] == s[r - 1]:
                r -= 1

            l += 1
            r -= 1

        if l > r:
            return 0

        return r - l + 1
