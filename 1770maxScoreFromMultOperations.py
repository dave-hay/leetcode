"""
 @param {number[]} nums
 @param {number[]} multipliers
 @return {number}
"""


class Solution:

    def maximumScore(self, nums, multipliers):
        numslength = len(nums)
        multiplierslength = len(multipliers)

        @lru_cache(2000)
        def dp(l, r):
            numsCurLen = r - l + 1
            iter = numslength - numsCurLen
            if iter > multiplierslength - 1: return 0

            mult = multipliers[iter]
            # have to return value only
            return max(mult * nums[l] + dp(l + 1, r),
                       mult * nums[r] + dp(l, r - 1))

        return dp(0, numslength - 1)
