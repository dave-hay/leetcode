class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            cur = nums[i]
            cur_idx = cur - 1
            if 1 <= cur <= n and cur != nums[cur_idx]:
                nums[cur_idx], nums[i] = nums[i], nums[cur_idx]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
