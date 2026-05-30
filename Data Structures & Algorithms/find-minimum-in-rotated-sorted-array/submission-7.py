class Solution:
    def findMin(self, nums: List[int]) -> int:

        # min=nums[0]   # suppose assigning min to 1st element

        # for i in range(1,len(nums)):
        #     if nums[i]<min:
        #         min=nums[i]
        # return min

        l=0
        r=len(nums)-1
        res=nums[0]
        while (l<=r):
            if nums[l]<=nums[r]:
                res=min(res,nums[l])
                break
            
            mid=(l+r)//2
            res=min(res,nums[mid])
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1

        return res
            


        



        