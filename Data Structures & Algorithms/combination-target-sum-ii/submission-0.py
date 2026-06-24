class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start,total,path):
            #base case
            if total == target:
                res.append(path.copy())
                return 
            if total > target:
                return 
            
            #process current node
            for i in range(start, len(candidates)):
                
                #pruning
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i-1]: # 如果有重复的，就跳过重复的
                    continue
                #process current node
                path.append(candidates[i])
                # keep exploring 
                dfs(i+1, total + candidates[i], path)
                # pop
                path.pop()

        dfs(0,0,[])
        return res
