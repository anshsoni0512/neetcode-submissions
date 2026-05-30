class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):  #range(4,4) produces nothing
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        d={}
        for i,n in enumerate(nums): #i is index and n is value in list nums
            diff=target-n
            if diff in d:  #in operator in diictonry check for key not for value
                return [d[diff],i]   #return indices not value  i is current index and d[diff] is index that is not current but present in hashmap
            else:
                d[n]=i   # IF DIFF IS NOT PRESENT THEN ADD ARRAYELEMNT TO HASHMAP

        
        
                
        