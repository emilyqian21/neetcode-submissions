# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(root, pathmax):
            # no return type dfs, traverse to update pathmax before current node
            if not root:
                return
            
            if pathmax <= root.val:
                self.count += 1

            dfs(root.left, max(pathmax, root.val))
            dfs(root.right, max(pathmax, root.val))
        dfs(root, -float('inf'))
        return self.count
