# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def dfs(node):
            # base case: 空节点里找不到答案
            if not node:
                return None

            # 1. 先去左子树找
            left = dfs(node.left)
            if left is not None:
                return left

            # 2. 处理当前节点
            self.count += 1
            if self.count == k:
                return node.val

            # 3. 再去右子树找
            right = dfs(node.right)
            if right is not None:
                return right

            # 4. 左、当前、右都没找到
            return None

        return dfs(root)