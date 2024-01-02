from collections import defaultdict


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mp = defaultdict(int)
        res = defaultdict(list)

        for i in nums:
            mp[i] += 1
            res[mp[i]].append(i)

        return res.values()
