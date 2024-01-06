class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        dp = [0] * (len(jobs) + 1)

        def binary_search(jobs, index):
            lo, hi = 0, index - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if jobs[mid][1] <= jobs[index][0]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo - 1

        for i in range(1, len(jobs) + 1):
            j = binary_search(jobs, i - 1)
            dp[i] = max(dp[i - 1], jobs[i - 1][2] + dp[j + 1])

        return dp[-1]
