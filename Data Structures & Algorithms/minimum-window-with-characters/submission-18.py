class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t=="":
            return ""

        l = 0
        tmap = {}
        wmap = {}
        res = [-1,-1]
        leng = float("infinity")

        for c in t:
            tmap[c] = tmap.get(c ,0)+1
        
        have = 0
        need =len(tmap) 

        for r in range(len(s)):
            c = s[r]
            wmap[c] = wmap.get(c,0)+1   # updating in the window map
            if c in tmap and wmap[c]==tmap[c]:   # c should be in t if its not in t we dont need to check if its not in t
                have = have+1
            while have==need:   # we found the pair 
                if r-l+1 < leng:

                    res = [l,r]
                    leng = r-l+1

                wmap[s[l]] = wmap[s[l]] - 1  # this startmetnes execute always wheather the leng is more or less

                if s[l] in tmap and wmap[s[l]] < tmap[s[l]]:   # if we removed a/b/c and it affects the have==need then do have = have -1 
                    have = have - 1
                l = l+1    # this statement will always be executed wheather the removed element was a/b/c or z

        
        if leng == float("infinity"):
            return ""
        else:
            return s[res[0]:res[1]+1]

                



        