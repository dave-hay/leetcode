class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = sum(nums)

        if total < target:
            return 0
        if total == target:
            return len(nums)

        l = cur = 0
        res = total

        for r in range(len(nums)):
            cur += nums[r]

            while cur >= target:
                res = min(r - l + 1, res)
                cur -= nums[l]
                l += 1

        return res
