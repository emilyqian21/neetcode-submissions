# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issametree(p ,q):
            # return boolean, if tree p and tree q are the same
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return issametree(p.left, q.left) and issametree(p.right, q.right)
        
        def subtree(root, subRoot):
            # return boolean, if root has a subtree same as subRoot
            if not subRoot:
                return True
            if not root and subRoot:
                return False

            res = issametree(root, subRoot) or subtree(root.left, subRoot) or subtree(root.right, subRoot)
            return res
        return subtree(root,subRoot)