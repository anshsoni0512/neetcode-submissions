class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Sort both list and then compare both list
        sList=list(s)
        tList=list(t)
        if sorted(sList)==sorted(tList): # no of elelmsnts and order matters when we check equals in list
            return True
        else:
            return False


        # sList=list(s)   #dont use split, it splits using space and we want each character
        # tList=list(t)

        # if sorted(sList)==sorted(tList):  #sList.sort() retuns none so none==none
        #     return True
        # else:
        #     return False
        

        # #sorted(sList) returns whole list with sorting

        # if len(s)!=len(t):
        #     return False

        # countS={}
        # countT={}

        # for chara in s:
        #     countS[chara]=1+countS.get(chara,0)   #updating values or creating if not present
        # for charar in t:
        #     countT[charar]=1+countT.get(charar,0)  #get method gives value of key

        # for c in countS:  # c is key
        #     if countS[c]!=countT.get(c,0): # what if c not present in countT then give 0
        #         return False
        # return True    #if all are equal then if block will not be executed and it will return true

        # if countS==countT:  #dict1 == dict2 Checks if all keys and values for each key are the same, order doesn’t matter
        #     return True
        # else:
        #     return False


        # tt=list(t)
        # if len(s)==len(t):
        #     for i in s:
        #         if i in tt:
        #             tt.remove(i)
        #         else:
        #             return False
        #     return True
        # return False        in this solution On^2 so not optimal

