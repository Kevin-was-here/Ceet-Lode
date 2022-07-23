"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

Example 1:

Input: s = "()"
Output: true

"""

def output(s:str) -> bool:
  open = []

  for i in s:
    if (i == "{" or i == "(" or i == "["):
      open.append(i)
    else:
      if len(open) == 0:
        return(False)
      elif(i == "}"): 
        if(open[len(open)-1] != "{"):
          return(False)
        else:
          open.pop(len(open)-1)
      elif(i == "]"): 
        if(open[len(open)-1] != "["):
          return(False)
        else:
          open.pop(len(open)-1)
      elif(i == ")"): 
        if(open[len(open)-1] != "("):
          return(False)
        else:
          open.pop(len(open)-1)
  
  if len(open) ==0:
    return True
  else:
    return False


s = input()
out = output(s)
print(out)

"""
Runtime: 46 ms, faster than 56.92% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 70.03% of Python3 online submissions for Valid Parentheses.
"""