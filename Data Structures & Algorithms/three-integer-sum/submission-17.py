class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        
#         for i in range(len(nums)):

#             for j in range(i+1,len(nums)):

#                 for k in range(j+1,len(nums)):
#                     if nums[i]+nums[j]+nums[k]==0:
#                         temp=sorted([nums[i],nums[j],nums[k]]) #sort the list
#                         res.add(tuple(temp))  # convert list into tuple  and add tuple in set as we cant add list 
#         return [list(i) for i in res] ## Result: [[-1, 0, 1], [-1, -1, 2]]
# #take each tuple and convert into list

        # Even with tuples in a set, you'll get 
        # duplicate triplets because [1, -1, 0] and [-1, 0, 1] 
        # are different tuples. You need to sort each triplet 
        # before adding it:


        sett=set()
        nums=sorted(nums)
        for i in range(len(nums)):
            l=i+1  # update everytime left and right pointer
            r=len(nums)-1
            while(l<r):
                sum=nums[i]+nums[l]+nums[r]
                if sum>0:
                    r=r-1
                elif sum<0:
                    l=l+1
                else:
                    sett.add(tuple([nums[i], nums[l], nums[r]]))
                    l=l+1
                    r=r-1
        return [list(i) for i in sett]




