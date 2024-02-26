class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #using the concept of effective buys
        profit  = 0
        effective = prices[0]

        i = 1

        while i < len(prices):
            profit = max(profit,(prices[i]- effective - fee))
            effective = min(effective, prices[i] - profit)
            i+=1
        
        return profit
        
