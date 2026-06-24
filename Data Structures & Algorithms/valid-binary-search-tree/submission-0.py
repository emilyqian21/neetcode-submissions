# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
    #dfs  逻辑最完整写法， preorder 
        def valid(node, left, right):
            # base case
            if not node:
                return True

            # current node
            current_valid = left < node.val < right

            # recurse
            left_valid = valid(node.left, left, node.val)
            right_valid = valid(node.right, node.val, right)

            # current result
            return current_valid and left_valid and right_valid

        return valid(root, float("-inf"), float("inf"))