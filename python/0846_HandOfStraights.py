import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}
        for n in hand:
            freq[n] = freq.get(n, 0) + 1

        nums = list(freq.keys())
        heapq.heapify(nums)

        while nums:
            first = nums[0]

            for cur in range(first, first + groupSize):
                # make sure freq
                if cur not in freq or freq[cur] < 1:
                    return False

                freq[cur] -= 1

                # decrement
                if cur == nums[0] and freq[cur] == 0:
                    heapq.heappop(nums)

        return True
