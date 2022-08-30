import heapq
from collections import Counter


class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


n = [1, 1, 1, 2, 2, 3]
k = 2
s = Solution()

print(s.topKFrequent(n, k))
