# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(root):
            # return depth of tree start from input"root"
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            # update self.res
            if abs(left - right) > 1:
                self.res = False

            cur = max(left, right) + 1
            return cur
            
        dfs(root)
        return self.res