"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Constraints:

    0 <= x <= 2^31 - 1

Example 1:

Input: x = 4
Output: 2

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""

def sqrtx(x):
  """
  x --> int
  rtype --> int
  """
  l = 0
  r = x
  while l <= r:
    mid = l + ((r-1)//2)

    if(x == 0):
      return 0
    
    if mid * mid <= x < (mid+1)*(mid+1): #case where sqrt(8) = 2.8... returns 2 
      return mid
    else:
      if(mid*mid > x): #greater means right is too big since right is the bigger value impacting solution
        r = mid -1
      else: #left is too small
        l = mid + 1

def main():
  x = 36548943165465
  sqrx = sqrtx(x)
  print(sqrx)


if __name__ == "__main__":
  main()


"""
init solution too shitty, gonna do binary search supposed to get good result but i guess my code is bad

actual good solution:
 def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1

binary search
x = 50
r = 10
l = 1
mid = 6
"""