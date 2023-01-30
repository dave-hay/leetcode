class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b, s = 0, 0

        while s < len(prices):
            # if sell > buy move buy to sell
            if prices[b] > prices[s]:
                b = s
                s += 1

            profit = max(profit, prices[s] - prices[b])
            s += 1

        return profit
