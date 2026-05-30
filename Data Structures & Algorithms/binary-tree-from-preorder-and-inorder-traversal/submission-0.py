# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        

        root = TreeNode(preorder[0])
        mid = self.search(preorder[0],inorder)
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:]) 

        return root

    def search(self, a, inorder):
        c = {}
        for index, value in enumerate(inorder):  # enumerate gives (index, value)
            c[value] = index
        return c[a]         # return AFTER loop finishes
    

        