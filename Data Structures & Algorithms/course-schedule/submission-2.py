class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # {course : prerequisite} e.g., {0:1, 1:0}
        premap = { i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)
        visited_this_path = set() #  我现在这条递归链上经过的数字

        def dfs(crs):
            #base case: when to stop search and return
            if crs in visited_this_path:
                return False # this course can't be taken
            if premap[crs] == []: # no prerequisite
                return True # this course can be taken 
            
            visited_this_path.add(crs)
            for r in premap[crs]:
                if dfs(r) == False: #if any requisite of the course can't be taken
                    return False  # return false

            #for loop 结束，所有 prerequisite 都检查完了，没有环
            visited_this_path.remove(crs)
            #记忆化，这门课可以修，所以直接变成[]
            premap[crs] = []
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True
            

