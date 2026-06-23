# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs
        self.res = 0 # make it self.res, so the res is accessible in the dfs function

        def dfs(node):
            #base case
            if not node:
                return 0 
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right)
            return max(left+1,right+1)

        dfs(root)
        return self.res    