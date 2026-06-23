# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

    
        #dfs 精简写法， time: O(N), space: O(N)     
        #base case
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root


        #dfs详细写法
                # def dfs(node):
        #     #base case
        #     if not node:
        #         return None
            
        #     #assume dfs works 
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     node.left, node.right = right, left
            
        #     return node

        # return dfs(root)  




        # #BFS: time O(N) space O(N)
        # #edge case
        # if not root:
        #     return None
        # queue = deque([root])

        # while queue:
        #     # for _ in range(len(queue)): #不需要分层结果的话，可以删掉这行
        #     curr = queue.popleft()
        #     curr.left, curr.right = curr.right, curr.left
        #     if curr.left:
        #         queue.append(curr.left)
        #     if curr.right:
        #         queue.append(curr.right)
        # return root
        

    
