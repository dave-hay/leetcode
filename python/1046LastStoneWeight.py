import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, (x - y))

        heap.append(0)
        return abs(heap[0])
