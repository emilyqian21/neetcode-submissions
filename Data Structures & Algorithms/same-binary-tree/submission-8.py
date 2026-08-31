# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return boolean, if tree start at p and tree start at q are same
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        # p.val == q.val 
        res = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return res
    