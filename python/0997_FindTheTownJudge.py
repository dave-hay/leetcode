class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        arr = [0] * (n + 1)

        for truster, trustee in trust:
            arr[truster] -= 1
            arr[trustee] += 1

        for trustee, count in enumerate(arr):
            if count == n - 1:
                return trustee

        return -1
