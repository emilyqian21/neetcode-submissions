# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #dfs, time O(n) space O（n)
        # self.res = True
        # def dfs(node):
        #     #base case
        #     if not node:
        #         return 0

        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     self.res = (self.res) and (abs(left - right) <= 1) #update self.res，如果有一个false，就会一直是false,因为false and true是false，false and false 还是false
        #     return max(left+1,right+1)#height

        # dfs(root)
        # return self.res

        #dfs return [t/f, height]
        def dfs(node):
            #base case
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            return [left[0] and right[0] and abs(left[1] - right[1]) <= 1, max(left[1]+1,right[1]+1)]

        return dfs(root)[0]