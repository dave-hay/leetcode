class Solution:
    """
    time: O(n+k)
    space: O(n+k)
    optimal solution and cur choice affects future opts
    """

    def deleteAndEarn(self, nums: List[int]) -> int:
        # sort or create a hashmap of num: total
        # iter trying each option start at smallest then either pick or pick next
        mp = {}
        sm = float("inf")
        lg = float("-inf")

        for n in nums:
            mp[n] = mp.get(n, 0) + n
            sm = min(sm, n)
            lg = max(lg, n)

        # start from smallest up
        # if cur + 1 doesn't exist then take cur
        # mp = {2: 4, 3: 9, 4: 4}
        # dp(i) = max(dp(i+2) + mp[i], dp(i+1))
        # dp(2) = max(dp(4) + mp[2], dp(3))
        # dp(4) = "biggest val so return"
        # dp(2) = max(4 + 4, 9)
        # start with smallest num

        @cache
        def dp(num):
            if num == lg:
                return mp[num]  # reached end
            if num > lg:
                return 0  # gone too far
            if num not in mp:
                while num not in mp:
                    num += 1

            return max(dp(num + 2) + mp[num], dp(num + 1))

        return dp(sm)


class Solution:
    """
    time: O(n + k)
    space: O(n)
    """

    def deleteAndEarn(self, nums: List[int]) -> int:
        mp = {}
        lg = 0

        for n in nums:
            mp[n] = mp.get(n, 0) + n
            lg = max(lg, n)

        prev2 = 0
        prev = mp.get(1, 0)

        for num in range(2, lg + 1):
            prev2, prev = prev, max(prev, prev2 + mp.get(num, 0))

        return prev
