# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
            



        # #bfs, time O(n) space O(n)
        # def bfs(node):
        #     #edge case
        #     if not node:
        #         return None
            
        #     queue = deque([node])
        #     res = []

        #     while queue:
        #         curr = queue.popleft()
        #         if curr == None:
        #             res.append(None)
        #             continue #跳过 queue.append(curr.left) queue.append(curr.right)
        #         else:
        #             res.append (curr.val)

        #         queue.append(curr.left)
        #         queue.append(curr.right)
        #     return res

        # return bfs(p) == bfs(q)