# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = collections.deque()

        if root==None:
            return []

        q.append(root)
        res = []
        while q:
            leng = len(q)
            level = []  
            for i in range(leng):
              
                node = q.popleft()
                if node:    # only insert values inside level if it is not null so level can never be null
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
          
            res.append(level)
        return res


# Before we start processing a level, we count how many nodes are in the queue — that count is exactly the number of nodes on that level.

# Why it's always correct:
# Queue starts with only root → level 1 has 1 node
# After processing level 1 → queue has exactly level 2's nodes
# After processing level 2 → queue has exactly level 3's nodes
            
                    
        