import heapq, math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        heap = []
        getDist = lambda x, y: math.sqrt(x**2 + y**2)

        for x, y in points:
            dist = getDist(x, y)
            heapq.heappush(heap, (-dist, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point[1] for point in heap]
