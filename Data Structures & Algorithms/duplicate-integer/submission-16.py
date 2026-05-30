class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # check every element with other
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        

        # #check if elemsnt exist in list if yes then duplicate, 
        # l=[]
        # for i in nums:
        #     if i in l:
        #         return True
        #     else:
        #         l.append(i)
        # return False


        #check length of st and list are same or not..
        hashset=set()  #definfing empty set
        #convert list into set 
        hashset=set(nums)
        if len(nums)==len(hashset):
            return False          #length same means no duplicate
        else:
            return True          #length different means duplicate

        
        

        