'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
'''

nums = [1,2,3,1]

def solve(arr):
    n = len(arr)
    prev = arr[0];
    prev2 = 0;

    for i in range(1, n):
        pick = arr[i];
        if (i>1):
            pick += prev2;
        nonPick = prev;
        cur_i = max(pick, nonPick);
        prev2 = prev;
        prev = cur_i;
    
    return prev;

def rob(nums):
    arr1, arr2 = [], []
    n = len(nums)

    if (n==1):
        return nums[0];

    for i in range(n):
        if(i!=0): arr1.append(nums[i])
        if(i!=n-1): arr2.append(nums[i])
    
    return max(solve(arr1), solve(arr2))

print(rob(nums))
    
