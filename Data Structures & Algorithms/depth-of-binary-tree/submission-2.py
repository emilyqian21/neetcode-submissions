# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # #dfs : time O(N) space O(N)
        # def dfs(node):
        #     #base case
        #     if not node:
        #         return 0
            
        #     #assume dfs works
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     return max(1+left, 1+right)
        # return dfs(root)

        #bfs time O(N) space O(N)
        #edge case:
        if not root:
            return 0
        queue = deque([root])
        res = 0

        while queue:
            for _ in range(len(queue)): # traverse every level
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            #end of this level
            res += 1
        return res
