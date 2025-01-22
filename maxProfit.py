class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minimumBuy = prices[0]
        for i in prices:
            result = max(result, i - minimumBuy)
            minimumBuy = min(minimumBuy, i)
        return result