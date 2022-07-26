"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are ordered from most
 significant to least significant in left-to-right order. The large integer does 
 not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Constraints:

  1 <= digits.length <= 100
  0 <= digits[i] <= 9
  digits does not contain any leading 0's.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

from re import I
from unicodedata import digit


def plusOne(digits):
  """
  digits -> list[int]
  return type -> list[int]
  """
  if digits[len(digits)-1] != 9:
    digits[len(digits)-1] += 1
    return digits
  else:
    i = len(digits)-1
    while digits[i] == 9:
      digits[i] = 0
      if i == 0:
        digits.insert(0,1)
        return digits
      else:
        i-= 1
    
    digits[i] += 1
  
  return digits

def main():
  digits =[4,3,2,1]
  print(plusOne(digits))

if __name__ == "__main__":
  main()

"""
Runtime: 24 ms, faster than 99.63% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 11.12% of Python3 online submissions for Plus One.
"""