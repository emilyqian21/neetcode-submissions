class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjcent dictionary
        course2pre = {}
        for c,p in prerequisites:
            if c not in course2pre:
                course2pre[c] = [] # initalize
            course2pre[c].append(p)

        def dfs(course, path):
            # 当前路径中再次遇到 course，说明存在环
            if course in path:
                return False

            # 没有 prerequisite，或者之前已经验证过
            if course not in course2pre or not course2pre[course]:
                return True

            path.add(course)

            for pre in course2pre[course]:
                if not dfs(pre, path):
                    return False

            path.remove(course)

            # Memoization：course 已验证不存在环
            course2pre[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True