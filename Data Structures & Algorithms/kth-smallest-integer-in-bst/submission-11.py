# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        
        self.res = float('inf')
        self.k = k
        def dfs(root):
            # traverse type, inorder traversal
            if not root:
                return
            
            dfs(root.left)

            self.k  -= 1
            if self.k == 0:
                self.res = root.val

            dfs(root.right)
            return
        dfs(root)
        
        return self.res