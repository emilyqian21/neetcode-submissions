# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k 
        self.res = float('inf')

        def dfs(root):
            # inorder traversal, nothing to return 
            # base case
            if not root:
                return 
            if self.k == 0:
                return
            
            # inorder traversal
            dfs(root.left)

            if self.k == 0:
                return 

            self.k -= 1
            self.res = root.val

            dfs(root.right)
            return 
        
        dfs(root)
        return self.res
