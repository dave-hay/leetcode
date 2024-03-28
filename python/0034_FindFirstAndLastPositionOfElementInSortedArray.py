class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        lo = findLeft(nums, target)
        hi = findLeft(nums, target + 1) - 1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]
