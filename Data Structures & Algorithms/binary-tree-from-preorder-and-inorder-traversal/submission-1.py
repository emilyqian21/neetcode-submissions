# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # dfs time o(n) space o(n)
        # value -> index in inorder
        # 用来 O(1) 找 root 在 inorder 里的位置
        #1. preorder 的第一个元素永远是当前 subtree 的 root
        # 2. inorder 中 root 左边是左子树，右边是右子树
        # 3. preorder 顺序是 root -> left -> right
        #    所以必须先 build left，再 build right
        idx_map = {val: i for i, val in enumerate(inorder)}

        # preorder 当前读到哪里了
        self.pre_idx = 0

        def dfs(left, right):
            # inorder[left:right] 这个区间没有节点了
            if left > right:
                return None

            # preorder 顺序是 root -> left -> right
            # 所以当前 pre_idx 指向的值，就是当前 subtree 的 root
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            # root 在 inorder 里的位置
            mid = idx_map[root_val]

            # inorder 里：
            # [left ... mid-1] 是左子树
            # [mid+1 ... right] 是右子树
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)