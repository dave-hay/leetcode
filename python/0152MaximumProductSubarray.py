class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for cur in nums:
            tmp = curMax * cur
            curMax = max(cur * curMax, cur * curMin, cur)
            curMin = min(tmp, cur * curMin, cur)
            res = max(res, curMax)
        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = sml = lrg = nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]
            tmplrg = max(cur, lrg * cur, sml * cur)
            sml = min(cur, lrg * cur, sml * cur)

            lrg = tmplrg

            res = max(lrg, res)

        return res
