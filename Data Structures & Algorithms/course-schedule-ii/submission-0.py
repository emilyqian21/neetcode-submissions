class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_to_pre = { i:[] for i in range(numCourses)} # {0:[],1:[]}
        for c,p in prerequisites:  #{0:[1],1:[2],2:[0]}
            course_to_pre[c].append(p)
        

        #for each dfs, keep a path_visited to detect if there is cycle in this path 
        # if one class is already checked to be okay to take, save it in checked set
        checked = set()
        path_visited = set()
        res = []

        def dfs(curr):
            #base case: when to stop searching and return 
            if curr in path_visited:
                return False
            if curr in checked:
                return True
            
            #valid node
            path_visited.add(curr)
            for p in course_to_pre[curr]:
                if dfs(p) == False: # if any of the pre has cycle so that the pre can't be taken
                    return False # this curr can not be taken as well
            

            #this node has been checked. it can be taken
            checked.add(curr) # this node can be taken
            path_visited.remove(curr) # the dfs for this curr path has been successful. remove the record now 
            res.append(curr)
            #return true
            return True
        
        # activate the dfs
        for c in range(numCourses):
            if dfs(c) == False: #if any of the course can't be taken, return []
                return [] 
        return res
