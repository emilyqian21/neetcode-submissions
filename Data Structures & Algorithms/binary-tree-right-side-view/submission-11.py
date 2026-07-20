# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # time: O(n)
        # space: O(h) worst case O(n) best case O(logn) for balance tree
        # 根据depth 来 找到level output
    
        res = []
        def dfs(root,depth):
            # base case
            if not root:
                return

            if depth == len(res):
                res.append(root.val) # first of the level
                # 从右往左扫
            right = dfs(root.right, depth + 1)
            left = dfs(root.left,depth + 1)

        dfs(root,0)
        return res
            
        