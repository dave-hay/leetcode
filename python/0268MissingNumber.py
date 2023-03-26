class Solution:
    """
    Brute:
        time: O(n^2)
        values to check are 0 -> len(nums) + 1
        loop and check if number is in nums, if not return missing

    Sort:
        time: O(n log n)
        sort it and if cur doesnt == cur - 1 return

    Compare sums:
        time: O(n)
        get sum of nums
        subtract by each integer in range
        return -(nums)
    """

    def missingNumber(self, nums: List[int]) -> int:
        # actual = sum(nums)
        # expected = int(len(nums) / 2 * (len(nums) + 1))
        # return expected - actual

        res = 0
        for n in nums:
            res += n

        for i in range(len(nums) + 1):
            res -= i

        return res * -1


class Solution:
    """
    XOR ^:
        time: 0(n)
        for int n, (n XOR n) == 0, ((n XOR n) XOR x) == x
        so if you XOR
    """

    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res ^ i + 1 ^ nums[i]

        return res
