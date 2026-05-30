# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:      # this means subroot has something and root is null then obviously False
            return False

        
        stack = [root]
        while stack:    # THIS IS DFS
            
            node = stack.pop()
            if self.sameTree(node,subRoot):    # if this condition is true then return true and get out of program
                return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False
            

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [(root,subRoot)]
        while stack:
            
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val!=node2.val:
                return False
            stack.append((node1.right,node2.right))
            stack.append((node1.left,node2.left))
        return True


        