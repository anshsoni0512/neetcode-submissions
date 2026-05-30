class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # res=0
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         leng=min(heights[i],heights[j])
        #         width=j-i
        #         area=leng*width
        #         res=max(area,res)  #compare new area to old max area
        # return res

#         # When i = 7:
# for j in range(i+1, len(heights)):  # range(8, 8)
#     # This creates an EMPTY range!
#     # range(8, 8) produces no values
#     # The inner loop doesn't execute at all
#THEN OUTER LOOP, I BECOMES 8 SO OUT OF OUTER LOOP(I DOES NOT BECOME 8 IT STOPS AS THE LEN=8)
        res=0
        l=0
        r=len(heights)-1
        while l<r:
           
            leng=min(heights[l],heights[r])
            width=r-l
            area=leng*width
            res=max(area,res)
            if heights[l]<heights[r]:
                l=l+1
            elif heights[l]>=heights[r]:
                r=r-1
        return res


        