class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find: time O(n * α(n))), n = node = edge, space O(n). 
        n = len(edges)
        node_to_par = { i : i  for i in range(n + 1)} # by default, the parent is itself
        rank = [1]*(n + 1)

        def find_root(node):
            # Base case：
            # 如果当前节点就是 root，就把 root 返回
            if node_to_par[node] == node:
                return node

            # Recursive：
            # 让 parent 去找真正的 root，
            # 并顺便把当前节点直接连到 root（Path Compression）
            node_to_par[node] = find_root(node_to_par[node])

            # 返回 root
            return node_to_par[node]
            # if node_to_par[node] != node: # if只执行一次， while不对； 简洁写法。和上面是同样的逻辑
            #     node_to_par[node] = find_root(node_to_par[node]) #return the root # path compression O（1）
            # return node_to_par[node]
            
        def union(n1,n2):
            r1, r2 = find_root(n1), find_root(n2)

            if r1 == r2: #cycle
                return False
            elif rank[r1] > rank[r2]: # use r1 as parent
                node_to_par[r2] = r1
                rank[r1] += rank[r2]
            else:
                node_to_par[r1] = r2
                rank[r2] += rank[r1]
            return True


        for n1, n2 in edges:
            if not union(n1,n2): # cycle 
                return [n1,n2]
