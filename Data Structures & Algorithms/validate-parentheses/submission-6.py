class Solution:
    def isValid(self, s: str) -> bool:
        

        # stack=[]

        # for i in range(len(s)):
        #     if s[i]=='(' or s[i]=='[' or s[i]=='{':  # the element is opening so add the element
        #         stack.append(s[i])
            
        #     else:  # we are at the element that is closing 
        #         if len(stack)==0:    # and the stack is empty so false
        #             return False
        #         elif s[i]==')' and stack[-1]=='(' or s[i]==']' and stack[-1]=='['or s[i]=='}' and stack[-1]=='{':
        #             stack.pop()
        #         else:
        #             return False  # if opening and closing dosent match

        # if len(stack)==0:
        #     return True
        # else:
        #     return False


        # close={')':'(',']':'[','}':'{'}
        # stack=[]
        # for i in s:
        #     if i in close.values():    # means i is an opening bracket
        #         stack.append(i)
        #     else:  # we are in closing bracket
        #         if len(stack)==0:  # means direct there is closing bracket so not true
        #             return False
        #         else:
        #             if close[i]==stack[-1]:  # closing and opening meetup
        #                 stack.pop()
        #             else:
        #                 return False   # opening and closing doesnt match
        # if len(stack)==0:
        #     return True
        # else:
        #     return False

        stack = []
        close = {')':'(','}':'{',']':'['}
        for i in s:
            if i in close.values(): # means it is in open bracket
                stack.append(i)
            else:   # means i is a close bracket 
                if len(stack)==0:
                    return False
                else:
                    if stack[-1]==close[i]:
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False





        
                
                
            
             
             
        
        