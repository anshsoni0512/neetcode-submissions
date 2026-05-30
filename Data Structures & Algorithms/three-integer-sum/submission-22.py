class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res=set()
        
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = (nums[i], nums[j], nums[k])
                        res.add(tmp)
        return [list(i) for i in res]  # convert list into tuple  and add tuple in set as we cant add list 
#          ## Result: [[-1, 0, 1], [-1, -1, 2]]
# #take each tuple and convert into list

        # Even with tuples in a set, you'll get 
        # duplicate triplets because [1, -1, 0] and [-1, 0, 1] 
        # are different tuples. You need to sort each triplet 
        # before adding it:


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




