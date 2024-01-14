'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
 You can only hold at most one share of the stock at any time. 
 However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

prices = [1,2,3,4,5]

def maxProfit(prices):
    #state: b or s
    # if b: i += 1
    # if s: i += 2, cooldown day

    #hashmap cache
    dp = {} #key= (i,buying) val = max profit

    def dfs(i,buying):
        if i >= len(prices): #out of bounds no profit
            return 0
        if (i, buying) in dp: #max profit associated with i is already calculated, 
            return dp[(i,buying)]
        
        if buying: #we can buy right now

            #--buying state--
            #max profit right now = max profit from remaining array - how much it costs if we buy right now
            buy = dfs(i+1, not(buying)) - prices[i]

            #--cooldown state--
            cooldown = dfs(i+1,buying) 

            #cache the result so we dont need to compute it again
            dp[(i,buying)] = max(buy,cooldown)
        else: #we can sell right now
            
            #--selling state--
            #max profit right now = max profit from remaining array + how much we get selling right now
            #note that index increase by 2 since we're selling
            sell =dfs(i+2, not buying) + prices[i] 

            #--cooldown state--
            cooldown = dfs(i+1,buying) 

            #cache the result so we dont need to compute it again
            dp[(i,buying)] = max(sell,cooldown)
        
        return dp[(i,buying)] #
    return dfs(0, True)

print(maxProfit(prices))