class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                leng=min(heights[i],heights[j])
                width=j-i
                area=leng*width
                res=max(area,res)
        return res

        