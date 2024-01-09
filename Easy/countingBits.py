'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
 ans[i] is the number of 1's in the binary representation of i.
'''

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    out = []

    # 2 parts to solution: 
    # 1. find the number of bits in each number
    # 2. find the number of 1s in each number
    for i in range(n+1):
        binary = bin(i)
        count1 = binary.count('1')
        out.append(count1)
    return out


n = 5
print(countBits(n))