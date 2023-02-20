class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            guess = nums[m]

            if target == nums[m]:
                return m

            # 1 3 6
            if guess > target:
                r = m - 1
            else:
                l = m + 1
        return l
