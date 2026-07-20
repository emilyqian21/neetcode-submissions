# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(root,pathmax): # return none
            # base case
            if not root:
                return
            
            #process current node
            if root.val >= pathmax:
                self.count += 1
            left = dfs(root.left, max(pathmax,  root.left.val if root.left else -float('inf') ))
            right = dfs(root.right, max(pathmax, root.right.val if root.right else -float('inf')))
        
        dfs(root,root.val)
        return self.count



