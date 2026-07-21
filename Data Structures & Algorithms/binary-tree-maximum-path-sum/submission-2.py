# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # bottom up dfs 
        self.res =  float("-inf") # 易错点，不能是0，如果都是负数
        def dfs(root): # return the max path sum
            # base case
            if not root:
                return 0
            
            left = dfs(root.left) 
            right = dfs(root.right)
            #update global record # 易错点，dfs return的是每个路线（只包含左+node, 右+node, node）， 不包含（左 + node + 右）
            self.res = max(self.res, root.val, left + right + root.val, left + root.val, right + root.val)
            return max(root.val, left + root.val, right + root.val)
            #进一步优化, 可以不用写那么多max
            # left = max(0, dfs(root.left))
            # right = max(0, dfs(root.right))
            # self.res = max(self.res, left + right + root.val)
            # return root.val + max(left, right)

        dfs(root)
        return self.res
