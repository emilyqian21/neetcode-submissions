# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bottom up dfs
        self.res = 0 # record the maximum diameters
        def dfs(node): # returns height
            # base case
            if not node:
                return 0 
            left = dfs(node.left) # left tree height
            right = dfs(node.right) # right tree height
            height = max(left, right) + 1
            diameter = left + right
            # update diameter
            self.res = max(self.res, diameter )
            return height
        dfs(root)
        return self.res