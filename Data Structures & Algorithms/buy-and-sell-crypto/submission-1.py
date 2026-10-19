class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = float('-inf')
        for i in range(len(prices)):
            minprice = min(minprice,prices[i])
            maxprofit = max(maxprofit,prices[i]-minprice)
        return maxprofit
        