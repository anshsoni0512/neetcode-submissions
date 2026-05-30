class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        c = {}
        l = 0
        leng = 0

        for r in range(len(s)):

            c[s[r]] = c.get(s[r],0) + 1
            while r-l+1 - max(c.values()) > k:   # not 'if' use 'while' becuase r should be there only not moving forward
                c[s[l]] = c[s[l]] - 1    # move left pointer forward so remove left vari value
                l = l+1
            leng = max(leng, r-l+1)
        return leng


        