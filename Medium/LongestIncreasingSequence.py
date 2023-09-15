nums = [10,9,2,5,3,7,101,18]
x = [1] * len(nums)

for i in range(1,len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            x[i] = max(x[i],x[j]+1)

print(max(x))