class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        c2pre = {}
        for c in range(numCourses):
            c2pre[c] =set()
        for c, pre in prerequisites:
            c2pre[c].add(pre)

        proven = set()
        def dfs(c, path):
            # dfs means if we can successfully take course c
            # base case
            if c in proven:
                return True
            if c in path:
                return False # cycle
                
            # main logic
            path.add(c)
            for pre in c2pre[c]:
                if not dfs(pre, path):
                    return False
            path.remove(c) 
            res.append(c) # postorder /topological sort
            proven.add(c) #memoization
            return True
            
        for c in range(numCourses):
            if not dfs(c,set()):
                return []
        return res
        
			