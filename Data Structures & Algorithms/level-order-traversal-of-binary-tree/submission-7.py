# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case
        if not root:
            return []

        q = deque([(root,0)])
        res = []

        while q:
            cur_node, depth = q.popleft()
            if depth == len(res):
                res.append([])
            res[depth].append(cur_node.val)

            if cur_node.left:
                q.append((cur_node.left, depth + 1))
            if cur_node.right:
                q.append((cur_node.right, depth + 1))

        return res