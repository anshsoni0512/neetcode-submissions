# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        stack = [(root,float("-infinity"),float("infinity"))]
        while stack:
            
            node, left, right = stack.pop()   # we pop here so we have to add in stack somewhere

            if not left<node.val<right:   # here if node is null then error is comming
                return False
            if node.left:      # dont append null values
                stack.append((node.left,left,node.val))
            if node.right:    # dont append null values
                stack.append((node.right,node.val,right))
        return True
            