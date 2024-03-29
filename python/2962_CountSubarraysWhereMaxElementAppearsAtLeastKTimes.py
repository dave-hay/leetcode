class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEl = max(nums)
        res = l = maxEls = 0

        # add all inc right then all inc left
        for r in range(len(nums)):
            if nums[r] == maxEl:
                maxEls += 1

            while maxEls == k and l <= r:
                if nums[l] == maxEl:
                    maxEls -= 1
                l += 1

            res += l

        return res
