class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        firstNSum = lambda n: int(n / 2 * (n + 1))

        i = res = count = 0

        while i < len(nums):
            if nums[i] == 0:
                while i < len(nums) and nums[i] == 0:
                    count += 1
                    i += 1

                res += firstNSum(count)
                count = 0
            else:
                i += 1

        return res
