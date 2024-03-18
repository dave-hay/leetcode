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


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[0])
        res = [points[0]]

        for p in points[1:]:
            a_start, a_end = res[-1]
            b_start, b_end = p

            # know a_start <= b_start
            if b_start <= a_end:
                res[-1] = [a_start, min(a_end, b_end)]
            else:
                res.append(p)

        return len(res)


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[0])
        res = [points[0]]

        for p in points[1:]:
            a_start, a_end = res[-1]
            b_start, b_end = p

            if (
                a_start <= b_start <= a_end
                or a_start <= b_end <= a_end
                or b_start <= a_start <= b_end
                or b_start <= a_end <= b_end
            ):
                res[-1] = [max(a_start, b_start), min(a_end, b_end)]
            else:
                res.append(p)

        return len(res)
