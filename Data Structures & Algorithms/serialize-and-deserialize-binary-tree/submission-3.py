# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # preorder traversal
        res = []
        def dfs(root):
            # traverse style, no return variable
            if not root:
                res.append('N')
                return 

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return
        
        dfs(root)
        return ','.join(res)    
    # Decodes your encoded data to tree.

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # use self.i to build tree
        data = data.split(",")
        self.i = 0
        def build():
            if self.i > len(data) - 1:
                return None
            if data[self.i] == 'N':
                self.i += 1
                return None

            root = TreeNode(int(data[self.i]))
           
            self.i += 1
            root.left = build()
            root.right = build()

            return root
          
        return build()

