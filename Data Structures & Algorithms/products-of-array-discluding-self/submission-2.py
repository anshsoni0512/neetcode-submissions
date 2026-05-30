class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

     l=[]
     for i in range(len(nums)):
        res=1
        for j in range(len(nums)):
            if i==j:
                j=j+1
            else:
                res=res*nums[j]
        l.append(res)   
     return l    