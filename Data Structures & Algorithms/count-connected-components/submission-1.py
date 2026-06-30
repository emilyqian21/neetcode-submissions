class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # time: O(V + E *alpha(V)) inverse Ackermann function (≈ constant in practice) SO Basically is O(V+E)
        # space: O(v)
        parent = [ i for i in range(n)] # the default parent is itself
        rank = [1] * n # rank is the size of the component; by default, it's just itself so it's 1 

        # parent = [0, 0, 1, 2]    3 → 2 → 1 → 0
        # Index:   0  1  2  3   
        def find_root(node): # find the root of the node, not the parent 
            curr_node = node # by default, the root is its self
            while parent[curr_node] != curr_node: # While the current node is not its own parent, it is not the root, so keep moving upward. # root node -->parent[cur] == cur
                parent[curr_node] = parent[parent[curr_node]] # Make my current node point to its grandparent. (This shortens the path.)
                # before parent[3] = parent[2] after the above line: parent[3] = 1, we skip 2. 
                # If the node doesn't have grandparent, will it cause error? --> No. Every node always has a parent. Even the root has a parent—it points to itself.
                # example: parent[node 1] = node 0, parent[node 0] = node 0, so parent[parent[node]] = node 0. 
                curr_node = parent[curr_node]  # now we move on to it's parents (1 now, we skip 2 by path compression) , continue searching. 
            return curr_node # after the while loop, we find the root. curr is the root now.


        def union(node1, node2):
            root_node1, root_node2 = find_root(node1), find_root(node2)

            if root_node1 == root_node2: # they already share the same root, so already connected. no need to union
                return 0 #  no union activated
            if rank[root_node1] > rank[root_node2]: # root of node1 bigger than root of node2, so root of node 2 will be the child
                parent[root_node2] = root_node1 # root_node2's parent will be root_node1
                rank[root_node1] += rank[root_node2] # update the root_node1's rank
                return 1 # if we performed union? yes. 
            else:
                parent[root_node1] = root_node2 # root_node2's parent will be root_node1
                rank[root_node2] += rank[root_node1] 
                return 1
            
        res = n # by default, there're n components. we don't know how many of them are connected
        for node1, node2 in edges:
            res -= union(node1,node2) # if we performed a union, it'll return 1, so we -1; if not return 0, -0
        return res

#mental model template
# class DSU:
#     def __init__(self, n):
#         # Initially, every node is its own parent (its own component)
#         self.parent = list(range(n))

#         # Size of each component (initially 1)
#         self.rank = [1] * n

#     def find(self, node):
#         """
#         Find the root (representative) of the component.
#         Uses path compression to flatten the tree.
#         """
#         cur = node

#         while cur != self.parent[cur]:
#             # Point current node to its grandparent
#             self.parent[cur] = self.parent[self.parent[cur]]

#             # Move upward
#             cur = self.parent[cur]

#         return cur

#     def union(self, node1, node2):
#         """
#         Merge the two components.
#         Returns True if a merge happened.
#         Returns False if they're already connected.
#         """
#         root1 = self.find(node1)
#         root2 = self.find(node2)

#         # Already in the same component
#         if root1 == root2:
#             return False

#         # Attach the smaller tree to the larger tree
#         if self.rank[root1] < self.rank[root2]:
#             root1, root2 = root2, root1

#         self.parent[root2] = root1
#         self.rank[root1] += self.rank[root2]

#         return True

