class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        def back(cur, seen):
            if len(cur) == len(nums):
                self.res.append(cur)
                return

            for i in range(len(nums)):
                if i in seen:
                    continue
                seen.add(i)
                back(cur + [nums[i]], seen)
                seen.remove(i)

        s = set()
        back([], s)
        return self.res
