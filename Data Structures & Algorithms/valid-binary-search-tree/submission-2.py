# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #bfs 
        if not root:
            return True

        queue = deque([( root, float("-inf"), float("inf") )]) #tuple(node, left boundary, right boundry)

        while queue:

            node,left,right = queue.popleft()

            if not( left < node.val < right):
                return False
            if node.left:
                queue.append((node.left,left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))
        return True




        # #dfs 减枝写法 pruning 
        
        # def valid(node,left,right):
        #     #base case
        #     if not node:
        #         return True
        #     #current node
        #     current_valid = left < node.val < right
        #     #pruning： 虽然还可以继续递归，但我已经知道最终答案了，所以没必要继续算。
        #     if current_valid == False:
        #         return False
            
        #     #left and right, recursive
        #     left_valid = valid(node.left, left, node.val)
        #     right_valid = valid(node.right, node.val, right)
        #     return left_valid and right_valid # 等价于return left_valid and right_valid and current_valid ，因为走到这一步 current_valid 已经是true了
        # return valid(root, float("-inf"), float("inf"))
    
    #dfs  逻辑最完整写法， preorder  time O(n) space O(n)
        # def valid(node, left, right):
        #     # base case
        #     if not node:
        #         return True

        #     # current node
        #     current_valid = left < node.val < right

        #     # recurse
        #     left_valid = valid(node.left, left, node.val)
        #     right_valid = valid(node.right, node.val, right)

        #     # current result
        #     return current_valid and left_valid and right_valid

        # return valid(root, float("-inf"), float("inf"))