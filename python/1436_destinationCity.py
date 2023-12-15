class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()
        ends = set()

        for start, end in paths:
            starts.add(start)

            if end not in starts:
                ends.add(end)

        for e in starts:
            if e in ends:
                ends.remove(e)

        return ends.pop()
