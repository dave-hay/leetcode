from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if k == len(nums) or len(nums) == 1:
            return [max(nums)]
        if k == 1:
            return nums

        q = deque()
        res = []

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        res.append(nums[q[0]])

        for i in range(k, len(nums)):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)
            res.append(nums[q[0]])

        return res


from collections import deque
import heapq


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if k == len(nums) or len(nums) == 1:
            return [max(nums)]
        if k == 1:
            return nums

        q = deque()
        res, heap = [], []

        # max heap so need to make opposite sign
        for i in range(k):
            cur = (nums[i] * -1, i)
            heapq.heappush(heap, cur)
            q.append(cur)

        res.append(heap[0][0] * -1)

        # if max == 1 then for next k iterations it will be the max
        for j in range(k, len(nums)):
            q.popleft()

            cur = (nums[j] * -1, j)
            heapq.heappush(heap, cur)
            q.append(cur)

            while heap[0][1] < q[0][1]:
                heapq.heappop(heap)

            res.append(heap[0][0] * -1)

        return res
