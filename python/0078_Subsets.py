class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def s(cur, i):
            nonlocal res

            if i == len(nums):
                res.append(cur[:])
                return

            s(cur, i + 1)
            s(cur + [nums[i]], i + 1)

        s([], 0)
        return res
