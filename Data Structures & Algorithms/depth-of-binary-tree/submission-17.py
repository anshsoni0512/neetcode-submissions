# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack = [(root,1)]
        result = 0
        while stack:

            node,depth = stack.pop()     # when we pop we calculate the max depth at that time
            if node:    # if this is null and we try to call null.right error so thats why write if statement
                result = max(result,depth)
                if node.right:
                    stack.append((node.right,depth+1))
                if node.left:
                    stack.append((node.left, depth+1))
        return result

        
        