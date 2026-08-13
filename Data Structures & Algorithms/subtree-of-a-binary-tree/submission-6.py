# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # return boolean, if it's subroot of root
        # base case
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False

        # main logic 
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return self.isSametree(root,subRoot) or left or right

        # return self.isSametree(root,subRoot) or self.isSametree(root.left,subRoot) or self.isSametree(root.right, subRoot)

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

        