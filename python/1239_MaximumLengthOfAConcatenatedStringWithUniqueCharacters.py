class Solution:
    def maxLength(self, arr) -> int:
        def can_concat(current, s):
            # Check if concatenating s to current results in unique characters
            if len(set(current + s)) == len(current) + len(s):
                return True
            return False

        def backtrack(index, current):
            nonlocal max_length
            if index == len(arr):
                max_length = max(max_length, len(current))
                return
            # Option 1: Skip the current string
            backtrack(index + 1, current)
            # Option 2: Include the current string if it doesn't introduce duplicates
            if can_concat(current, arr[index]):
                backtrack(index + 1, current + arr[index])

        max_length = 0
        backtrack(0, "")
        return max_length
