class Solution:
    """
    Greedy
    Time: O(n)
    Space: O(1)

    each loop we search a range to find the farthest we can go until end reached

    [2, 3, 1, 1, 4]
    1. start at first index [2] l=0, r=0, step=0
    2. from [2] possible range [3, 1] l=1, r=2, steps=1
    3. from [3, 1] possible range [1, 4] l=3, r=4, step=2
    """

    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

    def jumpMemoization(self, nums: List[int]) -> int:
        """
        Dynamic Programming
        Time: O(n^2)
        Space: O(n)
        """

        @cache
        def dp(i):
            if i >= len(nums) - 1:
                return 0
            # get possible step
            lowest = float("inf")
            for s in range(1, nums[i] + 1):
                x = dp(i + s) + 1
                lowest = min(lowest, x)
            return lowest

        return dp(0)
