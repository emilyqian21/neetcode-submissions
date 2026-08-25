class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adj dict 
        # find parents 
        # union 
        
        parent = [node for node in range(n)] # parent[i] = i as initialized, node is self parent
        rank = [1] * n 
        
        def find_parent(node):
            cur = node
            while parent[cur] != cur:
                parent[cur] = parent[parent[cur]] # path compression
                cur = parent[cur]
            return cur
        
        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2: # no need to union 
                return 0
            if rank[p1] > rank[p2]: # use p1 as parent
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        res = n
        
        for n1, n2 in edges:
            temp = union(n1, n2)
            res -= temp

        return res


