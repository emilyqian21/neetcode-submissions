class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph DFS（Cycle Detection）
        # time: O (V+E)
        # space: O(V+E)
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
            

 # dfs cycle detection 模版
    #  def dfs(node):

    #     # 1. 当前递归路径出现重复 -> 有环
    #     if node in visiting:
    #         return False

    #     # 2. 通过测试，没有cycle 
    #     if ...:
    #         return True

    #     # 3. 进入当前节点
    #     visiting.add(node)

    #     # 4. 递归所有邻居
    #     for nei in graph[node]:
    #         if not dfs(nei):
    #             return False

    #     # 5. 邻居都通过了测试，这条路已经通过了，把记录删掉，为下一条路准备
    #     visiting.remove(node)

    #     # 6. 记忆化
    #     premap[crs] = []
          # 7.返回这条路的结果--> 通过
    #     return True