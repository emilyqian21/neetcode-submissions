# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Interview Summary
        # Function	Time	Space
        # serialize	O(n) 	O(n)  --> data string  (auxiliary: O(h) --> recursion stack)
        # deserialize	O(n)	O(n) --> N tree nodes (auxiliary: O(h) ---> recursion stack)

        # where h is the height of the tree (O(log n) for a balanced tree, O(n) for a skewed tree)

        # preorder traversal
        self.res = []
        def dfs(node):
            #base case
            if not node:
                self.res.append("N")
                return
            #preorder
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ",".join(self.res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        self.i = 0
        data = data.split(",")

        def dfs():
            if data[self.i] == "N":
                self.i += 1 # update pointer
                return None
            
            # create nodes
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        tree = dfs()
        return tree