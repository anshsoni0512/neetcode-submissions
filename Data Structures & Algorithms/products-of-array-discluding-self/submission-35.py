class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

    #  l=[]
    #  for i in range(len(nums)): # i pointer is for every element 
    #     res=1  
    #     for j in range(len(nums)): # j pointer is for iterating all values for a single i value
    #         if i==j:
    #             j=j+1
    #         else:
    #             res=res*nums[j]
    #     l.append(res)   
    #  return l   



        # res=[1]*(len(nums))

        # prefix=1
        # for i in range(len(nums)):
        #     res[i]=prefix  # creating new res=[1,1,2,6]
        #     prefix=nums[i]*prefix #update prefix

        # postfix=1
        # for i in range(len(nums)-1,-1,-1):
        #     res[i]=res[i]*postfix  # multiply postfix with res value
        #     postfix=postfix*nums[i] # update postfix
        # return res

        # l = []
        
        # for i in range(len(nums)):
        #     result = 1
        #     for j in range(len(nums)):
        #         if i==j:
        #             j=j+1
        #         else:
        #             result = nums[j]*result
        #     l.append(result)
        # return l

        # Youre trying to assign to an index of an empty list.
        #  An empty list has no indices, so res[i] will throw an IndexError.
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix*nums[i]
            
        postfix = 1
        for i in range(len(nums)-1,-1,-1):   # dont stop at 0
            res[i] = postfix*res[i]
            postfix = nums[i]*postfix
            
        return res



        






















# Space Complexity: O(1) auxiliary space
# Total Space Used: O(n) (for the output, which we must return anyway)

# When someone says "this is O(1) space", they mean O(1) extra space beyond the output.
        
# Output space is excluded from space complexity analysis
# We only count auxiliary/extra space (working memory)        