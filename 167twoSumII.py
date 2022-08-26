class Solution:

    def twoSum(self, nums, target):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        low = 0
        high = len(nums) - 1

        while low < high:
            diff = nums[low] + nums[high]

            if diff == target:
                return [low + 1, high + 1]

            elif diff < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]
