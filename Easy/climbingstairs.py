"""

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 Constraints:

    1 <= n <= 45

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climb(n):
  a = b = 1
  for _ in range(n):
    a, b = b, a + b
  return a

def main():
  print(climb(5))

if __name__ == "__main__":
  main()

"""
for n = 5

1: a = 1, b = 2
2: a = 2, b = 3
3: a = 3, b = 5
4: a = 5, b = 8
5: a = 8, b = 13
"""