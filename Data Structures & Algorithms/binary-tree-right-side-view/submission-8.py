# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #dfs: 从右往左level traverse，只记录每个level第一个数字
        # self.res = []
        res = []
        def dfs(node,level):
            #base case 
            if not node:
                return 0
            
            #curr node
            if level == len(res): #self.res
                res.append(node.val) #因为这里只是修改res，所以不用写nonlocal，但如果是重新赋值 比如 res = [1]那么需要写nonlocal res
                # self.res.append(node.val)
            
            # right tree first, then left
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        
        dfs(root, 0)
        return res #self.res












        # #bfs精简版： time O(n) space O(n)
        # if not root:
        #     return []
        # global_res = []
        # queue = deque([root])

        # while queue:
        #     rightmost = None
        #     for _ in range(len(queue)):
        #         curr = queue.popleft()
        #         rightmost = curr.val #或者 if i == level_len - 1: res.append(curr.val)
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     global_res.append(rightmost)
        # return global_res




        # bfs ：只加这个level的最后一个数字
        # #edge case:
        # if not root:
        #     return []

        # global_res = []
        # queue = deque([root])

        # while queue:
        #     level_res = []
        #     for _ in range(len(queue)): #level 
        #         curr = queue.popleft()
        #         level_res.append(curr.val)

        #         # add left and right to queue
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     #end of this level
        #     global_res.append(level_res[-1])

        # return global_res
