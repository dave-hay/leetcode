class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if len(nums) < 2:
            return len(nums)

        seen = set(nums)
        longest = 1

        for i in range(len(nums)):
            if nums[i] - 1 in seen:
                continue

            inc = 1
            cur = 1
            while nums[i] + inc in seen:
                inc += 1
                cur += 1

            longest = max(cur, longest)

        return longest

    def longestConsecutive2(self, nums: List[int]) -> int:
        """
        Time Complexity: O(NlogN)
        Space Complexity: O(1)
        """
        if len(nums) < 2:
            return len(nums)
        # sort O(N * log N)
        nums.sort()

        longest = 1

        # start - i = len
        total = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] + 1 == nums[i + 1]:
                total += 1
            else:
                longest = max(total, longest)
                total = 1

        return max(total, longest)
