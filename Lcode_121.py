class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            
            if price < min_price:
                min_price = price
            
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
    
c =Solution()

print(c.maxProfit([7,1,5,3,6,4]))
