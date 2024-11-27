class Solution:
    def maximumProfit(self, prices):
        debt = -sys.maxsize
        profit = 0
        
        for p in prices:
            debt = max(debt, -p)
            profit = max(profit, debt + p)
        return profit
