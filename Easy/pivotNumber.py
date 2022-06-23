
nums = [-1,-1,-1,-1,-1,0]
S = sum(nums)
leftsum = 0
for i, x in enumerate(nums):
    if leftsum == (S - leftsum - x):
        pivotIndex = i
        found = True
        break
    leftsum += x
if not found:
    pivotIndex = -1

print(pivotIndex)