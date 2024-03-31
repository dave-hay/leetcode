class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left = right = 0
        min_pos = max_pos = -1

        while right < len(nums):
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
                min_pos = max_pos = -1
            else:
                if nums[right] == minK:
                    min_pos = right
                if nums[right] == maxK:
                    max_pos = right

                if min_pos != -1 and max_pos != -1:
                    count += min(min_pos, max_pos) - left + 1

            right += 1

        return count
