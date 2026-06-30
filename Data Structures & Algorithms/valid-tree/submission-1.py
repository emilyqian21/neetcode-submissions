class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #time: O(V+E) # space: O(V+E)
        #dfs cycle detection
        nodemap = {i:[] for i in range(n)} #{0:[],1:[]}
        for n1,n2 in edges:
            nodemap[n1].append(n2) # undirected edge, so both way. n1 is neibor of n2, n2 is also neighbor of n1
            nodemap[n2].append(n1)
        # edge case
        if not n:
            return False
        tree_visited = set()

        def dfs(curr,prev):
            #base case: when to stop searching and to return 
            if curr in tree_visited:
                return False
            
            #valid, process curr node
            tree_visited.add(curr)
            for nei in nodemap[curr]:
                if nei == prev: # 因为是双头edge, 1-->2-->3， 那 2 的nei就是1和3.我们不需要检查1，只需要检查3
                    continue #skip the prev
                if dfs(nei,curr) == False:
                    return False
            return True
        
           
        return dfs(0,-1) and  n == len(tree_visited)
