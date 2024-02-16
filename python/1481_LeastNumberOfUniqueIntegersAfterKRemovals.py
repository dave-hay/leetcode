import heapq
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """Counting Sort"""

        mp = {}
        for i in arr:
            mp[i] = mp.get(i, 0) + 1

        n = len(arr)

        freqs = [0] * (n + 1)

        for c in mp.values():
            freqs[c] += 1

        remaining = len(mp)

        for i in range(1, n + 1):
            toRm = min(k // i, freqs[i])

            k -= i * toRm

            remaining -= toRm

            if k < i:
                return remaining

        return 0


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """Sorting"""
        counts = Counter(arr)
        freqs = list(counts.values())
        freqs.sort()

        remaining = k
        res = len(freqs)

        for f in freqs:
            if f <= remaining:
                remaining -= f
                res -= 1
            else:
                return res

        return res


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """Heap"""
        freqs = Counter(arr)
        heap = list(freqs.values())

        heapq.heapify(heap)
        remaining = k

        for _ in range(len(freqs)):
            if heap[0] <= remaining:
                f = heapq.heappop(heap)
                remaining -= f

        return len(heap)
