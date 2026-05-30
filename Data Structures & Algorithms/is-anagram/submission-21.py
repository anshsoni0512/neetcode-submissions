class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sList=list(s)   #dont use split, it splits using space and we want each character
        # tList=list(t)

        # if sorted(sList)==sorted(tList):  #sList.sort() retuns none so none==none
        #     return True
        # else:
        #     return False
        

        # #sorted(sList) returns whole list with sorting

        if len(s)!=len(t):
            return False

        countS={}
        countT={}

        for chara in s:
            countS[chara]=1+countS.get(chara,0)   #updating values
        for charar in t:
            countT[charar]=1+countT.get(charar,0)

        if countS==countT:
            return True
        else:
            return False

