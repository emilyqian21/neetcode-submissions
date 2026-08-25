class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find
        # time: O (V + E*alpha(V))
        # space: O (V)

        parent = [ i for i in range(n)] # parent of itself
        rank = [1] * n 

        def find(node):
            cur_node = node
            while parent[cur_node] != cur_node:
                parent[cur_node] = parent[ parent[cur_node]] # path compression. set parent of cur_node = grandparent of cur_node
                cur_node = parent[cur_node]
            return cur_node # now cur_node is the root of node
        
        def union(n1,n2):
            parent_n1 = find(n1)
            parent_n2 = find(n2)

            if parent_n1 == parent_n2:
                return 0 # no union needed
            if rank[parent_n1] > rank[parent_n2]: # use parent_n1 as root  
                parent[parent_n2] =  parent_n1
                rank[parent_n1] += rank[parent_n2]
                return 1
            else:
                parent[parent_n1] =  parent_n2
                rank[parent_n2] += rank[parent_n1]
                return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1,n2)
        return res
