# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs
        #edge case
        if not root:
            return []

        queue = deque([root])
        global_output = []
        while queue:
            #level output
            level_output = []

            for _ in range(len(queue)):
                curr = queue.popleft()
                level_output.append(curr.val)
                #save left and right into queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # end of this level traversal
            global_output.append(level_output)
        return global_output