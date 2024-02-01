class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            a, b, c = nums[i : i + 3]

            if abs(a - b) <= k and abs(a - c) <= k and abs(b - c) <= k:
                res.append([a, b, c])
            else:
                return []

        return res
