# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # edge case
        if not root:
            return 0
            
        q = deque([root])
        depth = 0

        while q:
            for _ in range(len(q)):
                curnode = q.popleft()
                if curnode.left:
                    q.append(curnode.left)
                if curnode.right:
                    q.append(curnode.right)
            
            # end of level
            depth += 1

        return depth