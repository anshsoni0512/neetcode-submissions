class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # #Sort both list and then compare both list
        # sList=list(s)  #dont use split, it splits using space and we want each character
        # tList=list(t)   sList.sort() retuns none so none==none
        # if sorted(sList)==sorted(tList): # no of elelmsnts and order matters when we check equals in list
        #     return True
        # else:
        #     return False


        # #check if every element of s is present in t, if yes remove the lement from t and repeat this
        # tt=list(t)
        # if len(s)==len(t):
        #     for i in s:
        #         if i in tt:
        #             tt.remove(i)
        #         else:
        #             return False
        #     return True
        # else:
        #     return False        

        hashmap1={}
        hashmap2={}
        
            
            #create 2 hashmaps for 2 strings
        if len(s)==len(t):
            for i in s:
                hashmap1[i]=1+hashmap1.get(i,1)
            for j in t:
                hashmap2[j]=1+hashmap2.get(j,1)

                    #now compare 2 hashmaps
            for i in s:
                if hashmap1[i]==hashmap2.get(i,0):
                    continue
                else:
                    return False
            return True
        else:
            return False
        



            

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

