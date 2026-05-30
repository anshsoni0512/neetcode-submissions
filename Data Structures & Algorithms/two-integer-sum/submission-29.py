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



        # hashmap={}
        # for i in range(len(nums)):  #we have to work with index so we use index approach
        #     diff=target-nums[i]
        #     if diff in hashmap:  # in operator checks key-->  so in key we store element not index
        #         return [hashmap[diff],i]
        #     else:
        #         hashmap[nums[i]]=i  #add element and its index to hashmap



# What number do I still need to reach the target?”
# That number is:
# diff = target - nums[i]
# If we have seen that diff earlier, then we already found the pair.
# So we store numbers we have seen in a hashmap (dictionary) for fast lookup.
        
        
        
       

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
        
        h = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in h:
                return [h[diff],i]    # h[diff]  we have seen this before current i 
                
            else:
                h[nums[i]] = i
        
# h[diff] = index of an element we saw earlier (smaller index)
# i = current index (larger index)

        
                
        