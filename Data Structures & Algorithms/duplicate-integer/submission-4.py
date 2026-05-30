class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        sorted_nums=nums.sort()    
        print(sorted_nums)
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False


        