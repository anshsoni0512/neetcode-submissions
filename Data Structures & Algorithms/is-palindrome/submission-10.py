class Solution:
    def isPalindrome(self, s: str) -> bool:

        # res=''
        # for i in s:
        #     if i.isalnum():
        #         res=res+i.lower() 
        # if res==res[::-1]:  #here we have removed all apces, punctuaitons and lowercase done
        #     return True
        # else:
        #     return False

        l=0   # this is index
        r=len(s)-1  # this is index

        while l<r:

            while l<r and not(self.alphaNum(s[l])):
                l=l+1

            while l<r and not self.alphaNum(s[r]):
                r=r-1

            if s[l].lower()!=s[r].lower():
                return False
            l=l+1
            r=r-1
        return True





    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))