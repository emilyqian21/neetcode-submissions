# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # where h is the height of the tree.
        # Worst case: O(n)
        # Balanced tree: O(log n)
        
        self.count = 0
        
        def dfs(root,pathmax): # return none
            # base case
            if not root:
                return
            
            #process current node
            if root.val >= pathmax:
                self.count += 1
            # 更新路径最大值，递归传递给左右子树
            newmax = max(pathmax, root.val)
            left = dfs(root.left, newmax)
            right = dfs(root.right, newmax)
        
        dfs(root,root.val)
        return self.count



