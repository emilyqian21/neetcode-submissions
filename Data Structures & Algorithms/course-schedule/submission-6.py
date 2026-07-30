class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # linked list?
        # course2pre = { course: [pre] for course, pre in prerequisites}
        # print(course2pre)
        course2pre = {}
        for c,p in prerequisites:
            if c not in course2pre:
                course2pre[c] = []
            course2pre[c].append(p) # {1:[0,2],2:[3]} {0:[1],1:[0]} {0:[1]}
        
        visited_path = set() # 这条dfs path上visited过的

        def dfs(c): # return boolean
            # base case
            if c not in course2pre or not course2pre[c]:
                return True
            if c in visited_path:
                return False

            # process current node
            visited_path.add(c)
            for pre in course2pre[c]:
                if not dfs(pre):
                    return False

            # 这条path验证结束 (backtrack)
            visited_path.remove(c)
            #memoization for optimization
            course2pre[c] = [] # 这个课可以完成，下次不用跑了
            return True

        for c in range(numCourses):
            if not dfs(c): # 易错点，不是dfs(0),而是要检查所有课。因为可能有点课有loop，有的课没有loop
                return False
        return True


            
        