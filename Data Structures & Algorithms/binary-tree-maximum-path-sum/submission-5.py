# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxres = -float('inf')

        def dfs(root):
            # return maxpath of root.left or root.right, including itself 
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            cur = max(left,right,0) + root.val

            # update self.maxres
            self.maxres = max(self.maxres, root.val, root.val + left, root.val + right, root.val + left + right)
            return cur
        dfs(root)
       
        return self.maxres