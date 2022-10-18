class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        r = 1
        
        while r < len(prices):
          cur = prices[r] - prices[l]
          if(prices[r] < prices[l]):
            l = r
          else:
            best = max((prices[r] - prices[l]), best)           
          r+=1
                       
        return best