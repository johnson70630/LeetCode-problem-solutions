from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell-buy)
            else:
                buy = sell
        return profit
