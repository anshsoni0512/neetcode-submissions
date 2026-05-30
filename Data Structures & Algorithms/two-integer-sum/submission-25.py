class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #check every pair, if satisfies return true
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)): #range(4,4) produces nothing
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        

        # for i in range(len(nums)):
        #     j=target-nums[i]

        #     if j in nums:
        #         return [i,nums.index(j)]
        # return False

    
# in this there is one problem like duplication of number
#both numbers should be at different index, not on same index



        hashmap={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[nums[i]]=i
        

        
        
        
       

        # d={}
        # for i,n in enumerate(nums): #i is index and n is value in list nums
        #     diff=target-n
        #     if diff in d:  #in operator in diictonry check for key not for value
        #         return [d[diff],i]   #return indices not value  i is current index and d[diff] is index that is not current but present in hashmap
        #     else:
        #         d[n]=i   # IF DIFF IS NOT PRESENT THEN ADD ARRAYELEMNT TO HASHMAP


# Example:

# nums = [3,4,3], target = 6


# Without map:

# i = 0 → diff = 3 → diff in nums ✅
# nums.index(3) returns 0 (same element!) ❌ wrong result


# So you would return [0, 0], which is incorrect.

# The hash map solves this because it stores the index of a previously seen number, not just value existence.
        
        
                
        