class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest = 0
        left, right = 0, len(height) - 1

        while left < right:
            lh, rh = height[left], height[right]
            h = min(lh, rh)
            w = right - left
            largest = max(largest, w * h)

            # move the smallest verticle
            if lh < rh:
                left += 1
            else:
                right -= 1

        return largest
