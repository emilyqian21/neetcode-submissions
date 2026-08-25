class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node2nei = {}
        for node in range(n):
            node2nei[node] = []
        
        for node, nei in edges:
            node2nei[node].append(nei)
            node2nei[nei].append(node)
        
        q = deque([])
        visited = set()
        connect = 0

        for node in range(n):
            if node not in visited:
                q.append(node)
                visited.add(node)

                while q:
                    cur_node = q.popleft()
                    for nei in node2nei[cur_node]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                connect += 1
        
        return connect 