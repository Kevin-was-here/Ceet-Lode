"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day 
to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""

prices = [7,6,4,3,1]

def maxProfit(prices):
    left = 0 #buy index
    right = 1 #sell index
    maxProfit = 0

    while right < len(prices):
        
        if prices[left] < prices[right]:
            maxProfit = max(prices[right] - prices[left], maxProfit)
        else:
            left = right
        right += 1
    
    return maxProfit

print(maxProfit(prices))
