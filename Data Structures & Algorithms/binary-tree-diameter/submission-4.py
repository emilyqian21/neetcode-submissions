# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxres = 0

        def depth(root):
            # return the max depth of the tree start from input "root"
            if not root:
                return 0
            
            left = depth(root.left)
            right = depth(root.right)

            cur = max(left, right) + 1
            # calculate the diameter
            self.maxres  = max((left + right + 1), self.maxres)

            return cur


        depth(root)
        return self.maxres - 1


