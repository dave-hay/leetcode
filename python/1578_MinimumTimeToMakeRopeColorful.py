class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = curMax = 0

        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                curMax = 0

            res += min(curMax, neededTime[i])
            curMax = max(curMax, neededTime[i])

        return res


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0

        l = 0
        r = 1
        res = 0

        while r < len(colors):
            total = largest = neededTime[l]

            while r < len(colors) and colors[l] == colors[r]:
                largest = max(largest, neededTime[r])
                total += neededTime[r]
                r += 1

            res += total - largest
            l = r
            r += 1

        return res
