"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above
 (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""
s = "12"

def decodeWays(s):
    #use a dictionary(hasmap) to store the nodes (decision tree)
    #integers must be between 1-26
    #if the first number is 0, return 0

    #init the cache
    cache = {len(s): 1}

    def dfs(i): #takes an index
        if i in cache: return cache[i] #if the index is already in the cache, return the value
        if s[i] == "0": return 0 #invalid number

        res = dfs(i+1)
        if(i+1 < len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1]<="6"))): #if the next number is valid
            res += dfs(i+2)

        cache[i] = res #add the result to the cache
        return res
    return dfs(0)

print(decodeWays(s))