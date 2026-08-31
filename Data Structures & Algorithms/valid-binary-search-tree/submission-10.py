# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, low, high):
        # return boolean, if the tree start at intput"root" is a valid bst
            if not root:
                return True
            if not (low < root.val < high):
                return False
            
            left = dfs(root.left, low, root.val)
            right = dfs(root.right, root.val, high)
            return left and right
        return dfs(root, -float('inf'), float('inf'))
    