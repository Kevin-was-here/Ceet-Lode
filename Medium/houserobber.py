max= 0
nums = [1,2,3,4,5]
i = 0
while i <= len(nums)-2:
  if (nums[i] >= nums[i+1]):  
    max+= nums[i]
    i+=2
  else:  #nums[i] < nums[i+1]
    if nums[i+2] > nums[i+1]:
      max += nums[i] + nums[i+2]
      i+=3
      if i > len(nums)-1:
        print(max)
    else:
      max+= nums[i+1]
      i+=2
      if(i == len(nums)-1):
        max += nums[-1]
        print(max)
      else: print(max)
                