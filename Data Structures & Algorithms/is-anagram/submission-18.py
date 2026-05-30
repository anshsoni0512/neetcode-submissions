class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList=list(s)   #dont use split it splits using space
        tList=list(t)

        if sorted(sList)==sorted(tList):  #sList.sort() retuns none so none==none
            return True
        else:
            return False
        