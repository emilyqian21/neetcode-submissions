# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.k = k

        def dfs(root):
        # return none
        # inorder traverse 
        # base case
            if not root:
                return 
            
            # inorder traverse
            dfs(root.left)
            if self.k == 0: # 是在left之后就return，都不用去处理main node
                return
           
            self.k -= 1
            self.res = root.val

            dfs(root.right)
            return

        dfs(root)
        return self.res
            