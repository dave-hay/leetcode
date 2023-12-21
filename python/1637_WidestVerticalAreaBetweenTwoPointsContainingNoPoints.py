class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # width and height
        # point is inside if x > min or x < max and y < maxY or y > minY
        # one pass to find largest then check

        points.sort(key=lambda x: x[0])
        res = 0

        for i in range(1, len(points)):
            res = max(res, points[i][0] - points[i - 1][0])

        return res
