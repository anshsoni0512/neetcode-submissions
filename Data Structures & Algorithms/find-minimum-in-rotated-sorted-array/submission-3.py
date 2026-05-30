class Solution:
    def findMin(self, nums: List[int]) -> int:

        min=nums[0]   # suppose assigning min to 1st element

        for i in range(1,len(nums)):
            if nums[i]<min:
                min=nums[i]
        return min

        