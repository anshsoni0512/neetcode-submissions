class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # #Linear Search
        # for i in range(len(nums)):

        #     if nums[i]==target:
        #         return i
        # return -1


        # l=0
        # r=len(nums)-1

        # while l<=r : 

        #     mid=(l+r)//2
        #     if target==nums[mid]:
        #         return mid

        #     # we are in the left sorted array
        #     if nums[mid]>=nums[l]:
        #         if target<nums[l] or target>nums[mid]:
        #             l=mid+1   # go to right part
        #         else:
        #             r=mid-1   # go to left part
            

        #     #we are in the right sorted array
        #     else:
        #         if target<nums[mid] or target>nums[r]:
        #             r=mid-1  # go to left part
        #         else:
        #             l=mid+1  # go to right part

        # return -1   









        l = 0
        r = len(nums)-1

        while l<=r:

            

            mid = (l+r)//2   # once we find middle value then compare to target if not then do the whole procedure

            if nums[mid]==target:
                return mid     # return means get out of the function

            if nums[mid]>=nums[l]:   # we are in the left sorted part
                if target>nums[mid]:
                    l = mid+1
                elif target<nums[mid] and target<nums[l]:
                    l = mid+1
                elif target<nums[mid] and target>=nums[l]:
                    r = mid-1

            else:   # we are in the right sorted part
                if target<nums[mid]:
                    r = mid-1
                elif target>nums[mid] and target>nums[r]:
                    r = mid-1
                elif target>nums[mid] and target<=nums[r]:
                    l = mid+1
                       
        return -1
