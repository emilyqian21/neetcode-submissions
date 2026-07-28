"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new = {} # 易错点：不能用visited = set()，而是要用hashmap把存过的直接用


        def dfs(node): # return Node
            # base case
            if not node: # 易错点：不用写 not node.neighbor
                return None
            
            # process current node
            # if already has a copy, use that 
            if node in old2new:
                return old2new[node] # 已经存过所有neighbor信息了，不用keep exploring neighbor了
            # make a copy of current node
            else:
                copy = Node(val = node.val,neighbors = None)
                old2new[node] = copy

            # keep exploring
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) 
            return copy
        return dfs(node)
        
