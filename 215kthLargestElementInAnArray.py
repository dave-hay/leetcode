import heapq


class Solution:

    def findKthLargest(self, nums: list[int], k: int):

        return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
a = 5

s = Solution()
actual = s.findKthLargest(nums, k)
print(nums)
assert (actual) == a, f"got={actual}. expected={a}"
