"""
Given two strings text1 and text2, return the length of their longest common subsequence.
 If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters
 (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.
"""

text1 = "abcde"
text2 = "ace"

def longestCommonSubsequence(text1, text2):
    len1 = len(text1)
    len2 = len(text2)

    #Create a 2D array of size len1 x len2
    grid = [[0 for i in range(len2+1)] for j in range(len1+1)]

    #Iterate through the grid and check equals
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            #If the previous character is equal, add 1 to the diagonal
            if text1[i-1] == text2[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
            #Else, take the max of the left and top
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
    
    return grid[len1][len2]

print(longestCommonSubsequence(text1, text2))