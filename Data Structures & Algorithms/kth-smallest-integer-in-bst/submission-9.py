# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        n = 0
        curr = root


# curr is needed because when you move to the right subtree, the stack might be empty but there's still a node to visit.

        while curr or stack:     # curr can be false many times so use 'or' not 'and' and, initially stack is empty so you have to use curr with stack compulsory..
            while curr:             # when curr is null you can't go left and also when stack is empty you have to stop.. 
                stack.append(curr)
                curr = curr.left

            # if current is none means there is nothing on left so pop the element and increment 'n'

            curr = stack.pop()
            n = n+1
            if n==k:
                return curr.val
            
            # you have poped the middle part now go to right part 
            # sometimes you pop middle part then stack becomes empty so use both stack and curr in first while loop
            curr = curr.right
        

        