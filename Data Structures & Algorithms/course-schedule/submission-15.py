class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjcent dictionary
        course2pre = {}
        for c,p in prerequisites:
            if c not in course2pre:
                course2pre[c] = [] # initalize
            course2pre[c].append(p)
        
        # dfs
        def dfs(c,path):
            # dfs(c,path) means if we can succesfully take course c. path records all the course taken in this path before c
            # base case
            if c not in course2pre or not course2pre[c]: 
                return True
            if c in path:
                return False
            
            # main logic
            path.append(c)
            for pre in course2pre[c]:
                if not dfs(pre, path): # if any of pre returns false
                    return False
            #undo
            path.pop()

            # finish processing the current c 
            # if we reach here, there's no false
            course2pre[c] = [] # memoization, no need to process this c again
            return True
        
        for c in range(numCourses):
            if not dfs(c,[]):
                return False
        return True


        