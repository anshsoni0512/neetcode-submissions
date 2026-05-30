class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset=set(nums) # converting list into set
        longest=0
        for i in numset:
            if i-1 not in numset:  #if there is no left neighbour then len=1
                length=1
                while i+length in numset:
                    length=length+1
                longest=max(length,longest)
        return longest