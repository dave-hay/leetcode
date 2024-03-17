class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sums = {0: 1}
        res = 0
        cur = 0

        for n in nums:
            cur += n
            if cur - goal in sums:
                res += sums[cur - goal]

            sums[cur] = sums.get(cur, 0) + 1

        return res
