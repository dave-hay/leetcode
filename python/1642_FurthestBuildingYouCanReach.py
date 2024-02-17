import heapq


class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []  # Min-heap to store the gaps we've used ladders on
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
            if (
                len(heap) > ladders
            ):  # We've used more ladders than we have, replace one with bricks
                bricks -= heapq.heappop(heap)
            if bricks < 0:  # Ran out of bricks, can't move forward
                return i
        return len(heights) - 1  # We made it to the last building
