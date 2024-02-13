class Solution:
    def majorityElement(self, nums):
        """
        Boyer-Moore Voting Algorithm
        time: O(n)
        spce: O(1)
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
