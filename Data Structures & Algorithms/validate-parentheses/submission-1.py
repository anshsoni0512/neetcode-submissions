class Solution:
    def isValid(self, s: str) -> bool:
        

        stack=[]

        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':  # the element is opening so add the element
                stack.append(s[i])
            
            else:  # we are at the element that is closing 
                if len(stack)==0:    # and the stack is empty so false
                    return False
                elif s[i]==')' and stack[-1]=='(' or s[i]==']' and stack[-1]=='['or s[i]=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False

        if len(stack)==0:
            return True
        else:
            return False
                
                
            
             
             
        
        