# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs: only record the last value for each level
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            #level = []
            rightmost = None
            lenq = len(q)
            for i in range(lenq):
                cur = q.popleft()
                # level.append(cur.val)
                if i == lenq - 1 :
                    rightmost = cur.val 
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # end of level
            # res.append(level[-1])
            res.append(rightmost)
        return res