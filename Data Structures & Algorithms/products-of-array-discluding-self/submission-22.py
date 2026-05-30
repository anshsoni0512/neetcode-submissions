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



        res=[1]*(len(nums))

        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix=nums[i]*prefix

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=postfix*nums[i]
        return res






















# Space Complexity: O(1) auxiliary space
# Total Space Used: O(n) (for the output, which we must return anyway)

# When someone says "this is O(1) space", they mean O(1) extra space beyond the output.
        
# Output space is excluded from space complexity analysis
# We only count auxiliary/extra space (working memory)        