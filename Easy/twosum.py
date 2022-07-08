class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        second = 1

        #Good memory use but very slow solution
        while((nums[first]+nums[second] != target) or (first == second)):
            getAns = target - nums[first]
            try:
                second = nums.index(getAns)
                if second == first:
                    first += 1
            except ValueError:
                first+=1

        if first > second:
            temp = first
            first = second
            second = temp
        
        return [first,second]

#better solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for first, val in enumerate(nums):
            secondval = target - val
            if secondval in dic:
                return(dic[secondval], first)
            else:
                dic[val] = first