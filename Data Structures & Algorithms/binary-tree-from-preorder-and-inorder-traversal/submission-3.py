# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # time: O(n)
        # space: O(n), hashmap
        
        # root 在 inorder 里面的位置，用来切分 left subtree 和 right subtree。

        inorder_val2idx = { v:i for i, v in enumerate(inorder)} 
        preorder_idx = 0 # the current node

        def dfs(left,right):
            if left > right: # inorder[left：right] invalid
                return None
            
            # current node
            nonlocal preorder_idx
            cur_node_val = preorder[preorder_idx]
            preorder_idx += 1 # 易错点:没更新
            node = TreeNode(cur_node_val)
            # inorder [:node] 都是left tree, inorder[node + 1:]都是right tree
                  # split inorder
            mid = inorder_val2idx[cur_node_val]
            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)
            return node
        
        return dfs(0,len(inorder) - 1)
