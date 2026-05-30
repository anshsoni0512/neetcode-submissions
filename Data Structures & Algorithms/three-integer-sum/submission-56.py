class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
     
#Because nums is sorted:

# nums[i] ≤ nums[j] ≤ nums[k]

# Every triple is generated in sorted order:

# [-1,0,1]

# Only one version appears ✅

# That’s the main reason.
        # res = set()
         
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 l = [nums[i],nums[j],nums[k]]
        #                 l_sort = sorted(l)
        #                 res.add(tuple(l_sort))
        # return [list(i) for i in res]  # add tuple in set as we cant add list inside set 
#          ## Result: [[-1, 0, 1], [-1, -1, 2]]
# #take each tuple and convert into list because leetocde ask for list as output 

        # Even with tuples in a set, you'll get 
        # duplicate triplets because [1, -1, 0] and [-1, 0, 1] 
        # are different tuples. You need to sort each triplet 
        # before adding it:






# OPTIMAL SOLUTION

        # sett=set()
        # nums=sorted(nums)
        
        # for i in range(len(nums)):

        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
            
            
        #     l=i+1  # update everytime left and right pointer
        #     r=len(nums)-1
        #     while(l<r):
        #         sum=nums[i]+nums[l]+nums[r]
        #         if sum>0:
        #             r=r-1
        #         elif sum<0:
        #             l=l+1
        #         else:
        #             sett.add(tuple([nums[i], nums[l], nums[r]]))
        #             l=l+1
        #             r=r-1
        #             while l<r and nums[l]==nums[l-1]:
        #                 l=l+1
                
                
        # return [list(i) for i in sett]  




#         Why is it slow?
# The set + tuple conversion adds overhead:

# Converting list to tuple: tuple([nums[i], nums[l], nums[r]])
# Hashing the tuple for set insertion
# Converting back to list at the end: [list(i) for i in sett]
        set1 = set()
        nums = sorted(nums)

        
        
        i = nums[0]
        
     


        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue
            
            
            l = i+1
            r = len(nums)-1
            while l<r:
                
            
                if nums[i]+nums[l]+nums[r]>0:
                    r = r-1
                elif nums[i]+nums[l]+nums[r]<0:
                    l = l+1
                else:
                    set1.add((nums[i],nums[l],nums[r]))  #THIS IS A TUPLE
                    
                    l = l+1
                    
                    while l<r and nums[l]==nums[l-1]:
                        l = l+1
#Because duplicates matter only when:
# We’ve just recorded a solution
# And we want to avoid recording the same triplet again

        return[list(i) for i in set1] 

# Without skip loop
# Step
# Step
# Step
# Step
# With skip loop
# Step
# Jump Jump Jump
# Step
# THE NO OF ITERATION IS SAME AS OUTER WHILE LOOP, WE ARE JUST SKIPPING SOME STEPS

# Suppose n = 7

# Total possible l++ operations:

# 1
# 2
# 3
# 4
# 5
# 6

# That’s at most 6 increments total

# Those increments are split between:

# Main while loop

# Duplicate-skip loop

# But combined they can’t exceed 6.

# So cost is still:

# O(n)

# ⭐ The Rule I want you to remember

# This is GOLD for interviews:

# If a pointer only moves forward and never resets,
# count its total movement once — no matter how many loops move it.
