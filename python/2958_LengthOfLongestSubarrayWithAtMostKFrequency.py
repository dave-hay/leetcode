from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 1
        freqs = defaultdict(int)

        l = 0

        for r in range(len(nums)):
            # add cur
            cur = nums[r]
            freqs[cur] += 1

            while l < r and freqs[cur] > k:
                freqs[nums[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
