# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # node comes from preorder
        # range comes from inorder [left:idx] is the nodes to be added to left tree

        self.val2idx = {}
        
        for i, v in enumerate(inorder):
            self.val2idx[v] = i
        
        self.curidx = 0

        def dfs(left, right): 
            if left > right: # left pointer, right pointer. if left > right, then no node
                return None
            if self.curidx > len(inorder) - 1:
                return None

            cur_node_val = preorder[self.curidx]
            cur_node = TreeNode(cur_node_val)
            self.curidx += 1
            

            cur_node.left = dfs(left, self.val2idx[cur_node_val] - 1) 
            cur_node.right = dfs(self.val2idx[cur_node_val] + 1, right)

            return cur_node

        return dfs(0, len(inorder) - 1)
