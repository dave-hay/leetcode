import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 a day -> max pile
        lo, hi = 1, max(piles)
        fastest = h
        res = float("inf")

        while lo <= hi:
            curSpeed = (lo + hi) // 2

            # find total hours it will take to eat all
            # can exit early if goes over max hours

            curHours = 0

            for b in piles:
                curHours += math.ceil(b / curSpeed)

            if curHours > fastest:
                # need faster speed
                lo = curSpeed + 1
            else:
                # see if you can go slower and decrease res
                hi = curSpeed - 1
                res = curSpeed

        return res
