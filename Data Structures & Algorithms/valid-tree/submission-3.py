class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # time: O( V + E)
        # spcae: O( V + E)
        node2nei = {node : [] for node in range(n)}
        for no, nei in edges:
            node2nei[no].append(nei) # add into the dict
            node2nei[nei].append(no) # both direction

        visited = set()

        def dfs(node,prev):
            if node in visited:
                return False
            # if not node: # 易错点：这里写了就是错。如果node = 0，就是错的
            #     return True
            
            #process current node
            visited.add(node)
            for nei in node2nei[node]:
                if nei == prev: # don't repeat the way back 
                    continue 
                if not dfs(nei,node):
                    return False
            return True

        # for node in node2nei: #易错点：这里不需要；这个用法是在一个 graph 可能有多个 disconnected components，请判断每一个 component里有没有 cycle。
        #     if not dfs(node):
        #         return False
        return dfs(0,-1) and len(visited) == n
            
            