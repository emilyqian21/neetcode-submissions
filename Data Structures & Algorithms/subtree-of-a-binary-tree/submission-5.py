# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # top down dfs, return boolean;
        # helper function: bottom up dfs, return boolean

        # time: O(m*n) m = num of nodes in subRoot, n  = num of nodes in root; isSubtree visits each of the m nodes in root. At each node, it may call issametree. In the worst case, issametree compares all n nodes of subRoot.
        # space: O(n + m); This comes from the recursion stack. At any moment: isSubtree recursion can go as deep as the height of root: O(h₁) issametree recursion can go as deep as the height of subRoot: O(h₂) Since issametree is called during an isSubtree call, the maximum stack depth is: O(h1+h2)
        
        # base case
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.issametree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



    def issametree(self,p,q): # return boolean # 易错点：如果是self的话，需要和self的function indention一样；如果是内嵌的helper function的话，需要在用之前就define，且indention在里面
        # base case
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.issametree(p.left,q.left) and self.issametree(p.right,q.right)
    
    
