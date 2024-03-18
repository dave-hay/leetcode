class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = len(points)
        prev = points[0]

        for p in points[1:]:
            a_start, a_end = prev
            b_start, b_end = p

            # know a_start <= b_start
            if b_start <= a_end:
                res -= 1
                prev = [a_start, min(a_end, b_end)]
            else:
                prev = p

        return res
