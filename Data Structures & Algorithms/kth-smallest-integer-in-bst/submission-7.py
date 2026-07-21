# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time: without pruning --> O（n), with pruning --> O(h + k) average, O(n) worst case
        # Space: O(h), balance tree h = O(log n); worst ---> Space = O(n)
        self.count = k 
        self.res = 0
        def dfs(root): # just search, no need to return 
            # base case
            if not root  or self.count == 0:
                return
            
            dfs(root.left) # search left first
            self.count -= 1 # process current node
            if self.count == 0:
                self.res = root.val
                return # pruning:已经不用跑下面的dfs(root.right)了

            dfs(root.right) # search right 

        dfs(root)
        return self.res
        


