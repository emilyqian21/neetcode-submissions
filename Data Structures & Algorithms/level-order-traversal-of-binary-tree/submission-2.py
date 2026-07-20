# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        q = collections.deque([root])
        res = []
        # edge case:
        if not root:
            return []
        while q:
            level_res = []

            for _ in range(len(q)):
                cur = q.popleft()
                level_res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)


            # end of this level for loop
            res.append(level_res)
        return res