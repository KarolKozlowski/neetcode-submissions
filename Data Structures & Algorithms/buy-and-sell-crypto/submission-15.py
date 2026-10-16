class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy = prices[0]
        sell = prices[1]

        profit = sell - buy

        for i in range(1, len(prices) - 1):
            # print("buy: {}, sell: {}, profit: {}".format(buy, sell, profit))
            buy = min(prices[i], buy)
            sell = prices[i]
            sell = max(prices[i+1], sell)
            profit = max(sell - buy, profit)

        return profit if profit > 0 else 0