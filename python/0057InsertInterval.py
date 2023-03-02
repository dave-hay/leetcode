class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # edge cases
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                # overlapping
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        # two options
        res.append(newInterval)
        return res
