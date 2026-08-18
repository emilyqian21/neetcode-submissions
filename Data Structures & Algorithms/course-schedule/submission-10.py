class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time: O( V + E)
        # space: O( V + E)
        course2pre = {}
        for c,p in prerequisites:
            if c not in course2pre:
                course2pre[c] = []
            course2pre[c].append(p) # {1:[0,2],2:[3]} {0:[1],1:[0]} {0:[1]}
        
    

        def dfs(c, path): # return boolean; if we can take course c; path records all the nodes before current node; 
            # base case
            if c not in course2pre or not course2pre[c]:
                return True
            if c in path:
                return False

            # process current node
            path.append(c)
            # explore recurisvely, continue this path
            for pre in course2pre[c]:
                if not dfs(pre, path):
                    return False

            # 这条path验证结束 (backtrack)
            path.pop()
            #memoization for optimization
            course2pre[c] = [] # 这个课可以完成，下次不用跑了
            return True

        for c in range(numCourses):
            if not dfs(c,[]): # 易错点，不是dfs(0),而是要检查所有课。因为可能有点课有loop，有的课没有loop
                return False
        return True


            
        