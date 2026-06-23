# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs 
        def dfs(node):
            #base case
            if not node:
                return 0
            
            #assume dfs works
            left = dfs(node.left)
            right = dfs(node.right)
            return max(1+left, 1+right)
        return dfs(root)