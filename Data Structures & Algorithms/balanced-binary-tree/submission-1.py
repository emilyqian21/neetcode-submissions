# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #dfs
        self.res = True
        def dfs(node):
            #base case
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.res = (self.res) and (abs(left - right) <= 1) 
            return max(left+1,right+1)#height

        dfs(root)
        return self.res