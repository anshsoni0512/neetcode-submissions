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

            while l<r and not (self.alphaNum(s[l])):  # if not alphanum then skip but this thing we have to keep in loop increment left pointer till we get alphanumeric charatcer
                l=l+1

            while l<r and not (self.alphaNum(s[r])): #if not alphanum then skip
                r=r-1

            if s[l].lower()!=s[r].lower():  # check if both chaacter are same or not
                return False
            l=l+1 #increment pointer
            r=r-1 #decrement pointer
        return True


# s = "??a"
# l = 0, r = 2

# Skip ? → l = 1

# Skip next ? → l = 2

# Now l == r, but if we didn't check l < r inside the inner while, 
#we would continue and compare characters incorrectly or even access invalid indexes.


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))