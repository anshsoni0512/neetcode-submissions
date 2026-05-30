class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # #Sort both list and then compare both list
        # sList=list(s)  #dont use split, it splits using space and we want each character
        # tList=list(t)   sList.sort() retuns none so none==none
        # if sorted(sList)==sorted(tList): # no of elelments and order matters when we check equals in list
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
                hashmap1[i]=1+hashmap1.get(i,0) #updating values or creating if not present
            for j in t:
                hashmap2[j]=1+hashmap2.get(j,0) #get method gives value of key

            #now compare 2 hashmaps
            for i in s:
                if hashmap1[i]==hashmap2.get(i,0):  #what if any elment of s is not present in t so we have used get method so that it does not throw any error
                    continue
                else:
                    return False
            return True
        else:
            return False

    
        



            

        
        


    
