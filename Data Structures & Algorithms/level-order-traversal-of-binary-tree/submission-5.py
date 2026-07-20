# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # dfs
        # time: O(n)
        # space: O(n)
        res = []
        def dfs(root,depth): # return depth （height是从下往上， depth是从上往下）
            # base case
            if not root:
                return 
            # assume dfs work
            

            if depth == len(res):
               res.append([]) # new list
            res[depth].append(root.val)

            left = dfs(root.left,depth + 1)
            right = dfs(root.right, depth + 1)
            
            return 

        dfs(root,0)
        return res