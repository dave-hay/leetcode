class Solution:

    def twoSum(self, numbers, target):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]

            if total > target:
                r -= 1
            else:
                l += 1
