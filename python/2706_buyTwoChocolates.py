class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        s = [prices[0], prices[1]]

        for i in range(2, len(prices)):
            if prices[i] <= s[0] or prices[i] < s[1]:
                s[0] = min(s)
                s[1] = prices[i]

        return money - sum(s) if sum(s) <= money else money
