class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        highest_profit = 0

        for i, value in enumerate(prices):
            if value < lowest:
                lowest = value

            today_profit = value - lowest

            if today_profit > highest_profit:
                highest_profit = today_profit
        return highest_profit
            