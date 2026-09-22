class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = float('inf')
        maxprofit = float('-inf')
        for num in prices:
            minbuy = min(minbuy,num)
            maxprofit = max(maxprofit,num -minbuy)
        return maxprofit