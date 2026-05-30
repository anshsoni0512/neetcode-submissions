class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        
        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp=sorted([nums[i],nums[j],nums[k]])
                        res.add(tuple(temp))
        return [list(i) for i in res]


        # Even with tuples in a set, you'll get 
        # duplicate triplets because [1, -1, 0] and [-1, 0, 1] 
        # are different tuples. You need to sort each triplet 
        # before adding it: