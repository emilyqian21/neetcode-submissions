# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxval):
            #base case
            if not node:
                return 0
            
            #preorder 
            if node.val >= maxval:
                res = 1 #这里的res是局部变量，每次call dfs都会创一个新的res，但指代的不是同一个
            else:
                res = 0 
            maxval = max(maxval, node.val)
            res += dfs(node.left,maxval)
            res += dfs(node.right, maxval)
        
            return res
        return dfs(root,root.val)