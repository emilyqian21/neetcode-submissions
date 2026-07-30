class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # time: O( V + E)
        # space: O ( V + E)
        # TOPOLOGICAL SORT
        output = []
        checked = set() # have already put into ouput
        cycle = set() # path in this dfs search
        crs2pre = { c:[] for c in  range(numCourses)}
        for c,p in prerequisites: # 易错点，建完dict 忘记放东西进去了
            crs2pre[c].append(p)

        def dfs(c): # return boolean
            #base case
            if c in cycle:
                return False
            if c in checked:
            # if c in checked or c not in crs2pre or not crs2pre[c]: # 易错点：c不在crs2pre也要加入output，所以不能用这个条件
                return True 
            
            # process current node
            cycle.add(c)
            for pre in crs2pre[c]:
                if not dfs(pre):
                    return False
            
            # remove the c from the path and memorize the answer
            cycle.remove(c)
            checked.add(c)
            output.append(c) # topological sort
            return True # checked all pre, can take the class no cycle detected
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
