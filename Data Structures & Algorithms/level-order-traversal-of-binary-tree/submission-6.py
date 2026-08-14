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
            
        q = deque([root])
        res = []

        while q:
            level_output = []
            for _ in range(len(q)):  # level 
                cur_node = q.popleft()
                level_output.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            # end of this level
            res.append(level_output)

        return res