class Solution:
    def findMin(self, nums: List[int]) -> int:

        min = nums[0]
        for i in range(len(nums)):
            if nums[i]<min:
                min = nums[i]
        return min
        


        # l=0
        # r=len(nums)-1
        # res=nums[0]   # intialize any value as a minimum
        # while (l<=r):
        #     if nums[l]<=nums[r]:
        #         res=min(res,nums[l])
        #         break
            
        #     mid=(l+r)//2
        #     res=min(res,nums[mid])
        #     if nums[mid]>=nums[l]:   # we are in the left part so go to right part as small values lies in right part only!!
        #         l=mid+1
        #     else:
        #         r=mid-1          # we are already in right part so check if left ones are smaller or not

        # return res
            


        



        