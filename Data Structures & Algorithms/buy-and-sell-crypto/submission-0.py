class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = 0
        last = len(prices) - 1
        profits = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i] < prices[j] and i < j:
                    profits.append(prices[j]-prices[i])

        return max(profits) if len(profits) else 0
                