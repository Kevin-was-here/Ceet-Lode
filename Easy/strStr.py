"""
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Constraints:

  1 <= haystack.length, needle.length <= 104
  haystack and needle consist of only lowercase English characters

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

def strStr(haystack, needle) -> int:
  needleLen = len(needle) 
  if len(needle) == 0: return 0
  for i in range(len(haystack)):
    if haystack[i] == needle[0]:
      temp = haystack[i:i+needleLen]
      if(temp == needle):
        return i

  return -1

def main():
  haystack = "hello"
  needle = ""
  print(strStr(haystack,needle))

if __name__ == "__main__":
  main()

"""
Runtime: 41 ms, faster than 68.02% of Python3 online submissions for Implement strStr().
Memory Usage: 13.9 MB, less than 15.54% of Python3 online submissions for Implement strStr().
"""