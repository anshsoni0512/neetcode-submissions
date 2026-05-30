# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/2080ee6a-3d27-4cd5-0db2-07672ead8200/public$0


        curr = root
        while curr:
            if p.val<curr.val and q.val<curr.val:
                curr = curr.left
            elif p.val>curr.val and q.val>curr.val:
                curr = curr.right
            else:
                return curr