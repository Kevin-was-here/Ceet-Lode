'''
Given an integer n, return the number of strings of length n that consist 

only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
'''

#!Come back later

n = 2

#case n = 1
dp = [1,1,1,1,1]
prev = 5

#case n > 1
for i in range(1,n):
    
    #Count from the back
    for j in range(3,-1,-1): #from index 3 to 0
        #update the back value by adding it and its previous value (which is the sum of all the values before it)
        dp[j] = dp[j] + dp[j+1]
        prev += dp[j] #update the total

print(prev)