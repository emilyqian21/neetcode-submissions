class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        c2pre = {}
        for c in range(numCourses):
            c2pre[c] = []
        for c, pre in prerequisites:
            c2pre[c].append(pre)

        safe = set()

        def dfs(c, path):
            # dfs means if we can successfully take course c
            # base case
            if c in safe:
                return True
            if c in path:
                return False # cycle
                
            # main logic
            path.append(c)
            for pre in c2pre[c]:
                if not dfs(pre, path):
                    return False
            path.pop()
            res.append(c)
            safe.add(c)
            return True
            
        for c in range(numCourses):
            if not dfs(c,[]):
                return []
        return res
        
			