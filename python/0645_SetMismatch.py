class Solution:
    def findErrorNums(self, nums):
        duplicate = -1
        missing = 1
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]
