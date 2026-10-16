class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = prices[0]
        sell = prices[1]

        profit = 0

        for i in range(len(prices) - 1):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] < sell:
                sell = prices[i]
            if prices[i+1] > sell:
                sell = prices[i+1]

            if sell - buy > profit:
                profit = sell - buy

            print("buy: {}, sell {}, profit: {}".format(buy, sell, profit))
            print("buy: prices[{}]={}, sell: prices[{}]={}".format(i, prices[i], i+1, prices[i+1]))

        return profit