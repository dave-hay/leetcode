class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([s for s, _ in intervals])
        end = sorted([e for _, e in intervals])

        res = count = s = e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res
