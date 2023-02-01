class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = float("inf")
        l, r = 0, len(nums) - 1

        while l <= r:
            # shifted relm
            if nums[l] > nums[r]:
                m = (l + r) // 2
                smallest = min(nums[m], smallest)
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # do binary search
            else:
                return min(nums[l], smallest)
