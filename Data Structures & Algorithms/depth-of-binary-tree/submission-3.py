# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bottom up dfs
        # base case: when to stop searching and return answers
        # time: O(n)
        # space: O(n)
        if not root:
            return 0
        # assume dfs works
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        depth = max(left,right) + 1

        return depth