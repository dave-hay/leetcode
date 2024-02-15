class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        largest perim
        at least 3 sides
        longest < sideA + sideB + sidesN
        sideA < sum(sideA, sideB) and sideB < sum(sideA, sideB)
        perimeter = sum(sides)
        ---
        cuml = [0, 1, 2, 4, 7, 12, 24, 74]
        srt =  [1, 1, 2, 3, 5, 12, 50]
        nums = [1, 12, 1, 2, 5, 50, 3]
        res =  [0, 0, 0, 0, 0, 0, 12]
        """

        nums.sort()

        cuml = [0] * (len(nums))

        prev = 0
        for i, num in enumerate(nums):
            cuml[i] = prev
            prev += num

        for i in range(len(nums) - 1, -1, -1):
            if cuml[i] > nums[i]:
                return cuml[i] + nums[i]

        return -1


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """less space solution"""

        nums.sort()
        ans = -1
        prev = 0

        for i, num in enumerate(nums):
            if prev > num:
                ans = num + prev
            prev += num

        return ans
