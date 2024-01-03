class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = []

        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        arr = self.map[key]
        if timestamp < arr[0][0]:
            return ""
        elif arr[-1][0] < timestamp:
            return arr[-1][1]

        l, r = 0, len(arr)

        while l < r:
            m = (l + r) // 2
            mid = arr[m][0]
            if mid == timestamp:
                return arr[m][1]

            if mid < timestamp:
                l = m + 1
            else:
                r = m

        return "" if r == 0 else arr[r - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
