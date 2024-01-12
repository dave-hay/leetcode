class TimeMap:
    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vals:
            self.vals[key] = list()

        # can append bc increasing
        self.vals[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        cur = self.vals.get(key, None)

        if not cur or timestamp < cur[0][0]:
            return ""

        # time too large, return largest value
        if timestamp > cur[-1][0]:
            return cur[-1][1]

        l, r = 0, len(cur)
        while l <= r:
            m = l + (r - l) // 2
            mid = cur[m]

            if timestamp == mid[0]:
                return mid[1]

            if timestamp > mid[0]:
                l = m + 1
            else:
                r = m - 1

        return cur[r][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
