# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 利用BST的特性，左边的都小于node,右边的都大于node;如果是common ancester, 那么P一定在node左边，Q一定在node 右边；或者P = node or Q = node

        # time: O(h)
        # space: O(1)
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val: # 都在左边
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val: # 都在右边
                cur = cur.right
            else : # p和q在cur的两侧 或者 p和q其中等于 cur
                return cur
            