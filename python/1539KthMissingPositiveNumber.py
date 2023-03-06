class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k <= arr[0] - 1:
            return k
        k -= arr[0] - 1

        for i in range(len(arr) - 1):
            cur = arr[i + 1] - arr[i] - 1
            if k <= cur:
                return arr[i] + k

            k -= cur
        return arr[-1] + k
