class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        l = 0
        res = [-1,-1]
        leng = float('infinity')

        tmap = {}
        for i in t:
            tmap[i] = tmap.get(i,0) + 1
        need = len(tmap)

        w = {}
        have = 0
        for r in range(len(s)):
            w[s[r]] = w.get(s[r],0) + 1

            if s[r] in tmap and w[s[r]] == tmap[s[r]]:
                have = have+1

            while have == need:   # first check length 
                if r-l+1 < leng:
                    leng = r-l+1
                    res = [l,r]


                if s[l] in tmap:
                    w[s[l]] -= 1
                    if w[s[l]] < tmap[s[l]]:
                        have -= 1
                l = l+1
            
            
        
        if leng<float("infinity"):
            return s[res[0]:res[1]+1]
        else:
            return ""
        


                



        