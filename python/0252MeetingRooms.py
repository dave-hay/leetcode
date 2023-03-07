class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda i: i[0])

        lrg = intervals[0][1]
        for start, end in intervals[1:]:
            if lrg > start:
                return False
            else:
                lrg = end
        return True
