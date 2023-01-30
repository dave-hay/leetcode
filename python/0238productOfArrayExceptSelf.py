class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)
        total = 1

        for i in range(len(nums)):
            answer[i] *= total
            total *= nums[i]

        total = 1
        for j in range(len(nums) - 1, -1, -1):
            answer[j] *= total
            total *= nums[j]

        return answer
