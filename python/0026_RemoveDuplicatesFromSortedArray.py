class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        pointer to new index and return that
        k: points to insetion location
        i: current index
        nums[0] always ok
        """
        k = 1
        i = 1
        prev = nums[0]

        while i < len(nums):
            if nums[i] != prev:
                nums[k] = nums[i]
                prev = nums[i]
                k += 1
            i += 1

        return k
