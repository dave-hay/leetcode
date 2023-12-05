import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        time: O(N + k log N)
        space: O(N)
        """
        counts = Counter(words)
        heap = [(-freq, word) for word, freq in counts.items()]

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
