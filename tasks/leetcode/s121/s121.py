class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        mini = len(prices) - 1
        maxi = mini

        while mini >= 0:
            profit = max(profit, prices[maxi] - prices[mini])

            if prices[mini] > prices[maxi]:
                maxi = mini

            mini = mini - 1

        return profit
