class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            i = abs(num) - 1

            if nums[i] > 0:
                nums[i] *= -1
            else:
                res.append(i + 1)

        return res
