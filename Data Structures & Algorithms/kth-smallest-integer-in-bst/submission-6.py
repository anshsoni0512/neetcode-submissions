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

        while curr or stack:     # curr can be false many times so use 'or' not 'and'
            while curr:             # when curr is null you can't go left and also when stack is empty you have to stop.. 
                stack.append(curr)
                curr = curr.left
            # if current is none pop the element

            curr = stack.pop()
            n = n+1
            if n==k:
                return curr.val
            curr = curr.right
        

        