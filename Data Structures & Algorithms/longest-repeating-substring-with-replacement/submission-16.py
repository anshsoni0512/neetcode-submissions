class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        c = {}
        result = 0
        l = 0

        for r in range(len(s)):

            c[s[r]] = c.get(s[r],0) + 1
            while r-l+1 - max(c.values()) > k:
                c[s[l]] = c[s[l]] - 1
                l = l+1
            result = max(result,r-l+1)
        return result




# MOVE LEFT POINTER UNITLL THE WINDOW LENG - MOST FREQ ELEMTN <= k 

        