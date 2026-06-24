# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #recursive dfs, 最完整的逻辑， 比上一种pruning更彻底，推荐写这种。time O(n) space O(n)
        self.count = 0

        def dfs(node): # dfs(node) 返回值的意义：在 node 这棵子树里：找到了答案 -> 返回答案 没找到答案 -> 返回 None
            # base case: 空节点里找不到答案
            if not node: # 空树没找到答案,return None
                return None

            # 1. 先去左子树找
            left = dfs(node.left) 
            if left is not None: #如果左树找到答案，直接上传答案
                return left

            # 2. 处理当前节点
            self.count += 1
            if self.count == k:  # 如果当前节点就是答案，直接上传答案
                return node.val

            # 3. 再去右子树找
            right = dfs(node.right) 
            if right is not None: #如果右树是答案，直接上传答案
                return right

            # 4. 左、当前、右都没找到 #上传没找到答案，None
            return None

        return dfs(root)

#     3
#    / \
#   2   4
#  /
# 1
# k  = 1

# dfs(3)
# → 先去左边 dfs(2)

# dfs(2)
# → 先去左边 dfs(1)

# dfs(1)
# → 先去左边 dfs(None)
# → 返回 None

# 回到 1
# → left 是 None
# → count += 1，count = 1
# → count == k
# → return 1
# 回到 dfs(2)

# left = dfs(1) 得到 1
# left is not None
# → return 1
# 回到 dfs(3)

# left = dfs(2) 得到 1
# left is not None
# → return 1
# 最终 return dfs(root) = 1 
# 真正处理 count 的节点：只有 1
# 走过调用路径的节点：3 → 2 → 1
# 完全没访问的节点：4


        
#         #recursive dfs, 简洁写法，这个版本不会跑完所有节点
#         self.k = k
#         self.res = None

#         def inorder(node):
#             if not node or self.res is not None: #假设k = 1, inorder(node.right)还是需要跑，但是在开头这里就可以直接return，不用跑其他的了
#                 return

#             inorder(node.left)

#             self.k -= 1
#             if self.k == 0:
#                 self.res = node.val
#                 return

#             inorder(node.right)

#         inorder(root)
#         return self.res
# #     3
# #    / \
# #   2   4
# #  /
# # 1
# # k  = 1
# # 访问 3 的左边
# # 访问 2 的左边
# # 访问 1
# # 找到答案 1

# # 回到 2，看到 res 已经有了，return
# # 回到 3，看到 res 已经有了，return

# # 不会访问 4
# #它会回到递归栈上的祖先节点，但不会继续访问新的无关节点

