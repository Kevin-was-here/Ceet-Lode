"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

s = "caac"


def countSubstrings(s):

    out = 0
    for i in range(len(s)):

        l = i
        r = i

        #odd case
        while l > -1 and r < len(s):
            
            if s[l] == s[r]:
                out+=1
            else:
                break

            l = l - 1
            r = r + 1

        #even case
        l = i
        r = i+1

        if r < len(s) and s[l] == s[r]:
           while l > -1 and r < len(s):
            
            if s[l] == s[r]:
                out+=1
            else:
                break

            l = l - 1
            r = r + 1

    return out

print(countSubstrings(s))