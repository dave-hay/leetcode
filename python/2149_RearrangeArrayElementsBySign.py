class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        # pointers to indexes
        pos, neg = 0, 1

        for i, n in enumerate(nums):
            if n < 0:
                ans[neg] = n
                neg += 2
            else:
                ans[pos] = n
                pos += 2

        return ans
