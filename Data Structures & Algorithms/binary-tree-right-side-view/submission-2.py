# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #edge case:
        if not root:
            return []

        global_res = []
        queue = deque([root])

        while queue:
            level_res = []
            for _ in range(len(queue)): #level 
                curr = queue.popleft()
                level_res.append(curr.val)

                # add left and right to queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            #end of this level
            global_res.append(level_res[-1] if level_res else None)

        return global_res
