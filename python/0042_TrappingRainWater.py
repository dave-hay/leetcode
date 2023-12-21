class TwoPointer:
    def trap(self, height: List[int]) -> int:
        """
        time: O(n)
        spce: O(1)
        """
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


class DynamicProgramming:
    def trap(self, height: List[int]) -> int:
        """
        time: O(n)
        spce: O(n)
        """
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])

        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(height[i + 1], maxRight[i + 1])

        maxHeight = [min(maxRight[i], maxLeft[i]) for i in range(len(height))]

        res = 0

        for i, h in enumerate(height):
            if h < maxHeight[i]:
                res += maxHeight[i] - h

        return res
