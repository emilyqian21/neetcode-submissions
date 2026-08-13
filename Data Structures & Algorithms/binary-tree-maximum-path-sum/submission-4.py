# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1 * float('inf')
        def dfs(root):
            #return max path without split
            if not root:
                return 0
            
            left = dfs(root.left)
            right =dfs(root.right)
            left_max = max(0,left)
            right_max = max(0,right)

            # record max with split
            self.res = max(self.res, root.val + left_max + right_max)
            #return max path without split
            return max(left_max, right_max) + root.val
        dfs(root)
        return self.res

