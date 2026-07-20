# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #top down dfs
        def dfs(root, low, high): # return boolean
            # base case
            if not root:
                return True 

            if not low < root.val < high:
                return False
            
            left = dfs(root.left, low, root.val)
            right = dfs(root.right, root.val, high)

            return left and right # 汇总答案
        return dfs(root, -float('inf'),float('inf'))
            