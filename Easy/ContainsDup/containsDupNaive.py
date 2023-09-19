class Solution:
    def containsDuplicate(self, nums) -> bool:
        
        in_list = {}

        for i in nums:
            if i in in_list.keys():
                return True
            else: in_list[i] = ""
        
        return False
