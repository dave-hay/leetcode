class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        time: O(n logn)
        space: O(1)

        optimized by just tracking the last interval
        """
        intervals.sort(key=lambda i: i[0])

        res = 0
        last = intervals[0][1]

        for start, end in intervals[1:]:
            if start < last:
                res += 1
                last = min(end, last)
            else:
                last = end

        return res


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        time: O(n logn)
        space: O(n)
        """
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda i: i[0])

        res = 0
        cur = [intervals[0]]

        for start, end in intervals[1:]:
            last = cur[-1][1]

            if last == start:
                cur[-1][1] = end
            elif start < last:
                res += 1
                cur[-1][1] = min(end, last)
            else:
                cur.append([start, end])

        return res
