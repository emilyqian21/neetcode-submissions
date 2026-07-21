# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k 
        self.res = 0
        def dfs(root): # just search, no need to return 
            # base case
            if not root:
                return
            
            dfs(root.left) # search left first
            self.count -= 1 # process current node
            if self.count == 0:
                self.res = root.val
            dfs(root.right) # search right 

        dfs(root)
        return self.res
        


