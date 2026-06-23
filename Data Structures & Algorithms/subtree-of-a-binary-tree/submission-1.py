# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and not subRoot:
            return True
        
        if self.isSametree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSametree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root and subRoot and root.val != subRoot.val:
            return False

        left = self.isSametree(root.left, subRoot.left)
        right = self.isSametree(root.right, subRoot.right)
        return left and right

        