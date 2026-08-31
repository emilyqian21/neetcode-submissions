# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder is the node for root; inorder[root] left is left tree nodes, right is right tree nodes
        node2idx = {} # for inorder list
        for i, n in enumerate(inorder):
            node2idx[n] = i

        self.inorderidx = 0
        def build(left, right):
            # return treenode start from input "root"
            if left > right:
                return None
            if self.inorderidx > len(inorder) - 1:
                return None

            cur_val = preorder[self.inorderidx]
            cur = TreeNode(cur_val, left = None, right = None)
            self.inorderidx += 1

            root_idx = node2idx[cur_val] # if root = 1, root_idx = 1
            cur.left = build(left, root_idx - 1)
            cur.right = build(root_idx + 1,right)

            return cur
       
        return build(0, len(inorder) - 1)