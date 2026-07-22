class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # set不能存list
        path = []
        candidates.sort()

        def dfs(start,pathsum):
            # record answer when valid 易错点：应该先判断这个条件，而不是start == len(nums)
            if target == pathsum:
                res.append(path.copy())
                return
            # base case
            if start == len(candidates):
                return

            
            # choose number
            for i in range(start,len(candidates)): # 防止[1,2,3],[2,1,3]这种permutation的情况
                # choose number
                # deduplicate
                if  i > start and candidates[i] == candidates[i-1]: # 假设nums [ 1,1,1,2]防止[1,1,2],[1,1,2]重复出现
                    continue
                # pruning
                if candidates[i] + pathsum > target:
                    continue
                path.append(candidates[i])
                # explore the path
                dfs(i + 1,pathsum + candidates[i]) # 只能用一次
                # undo
                path.pop()
        dfs(0,0)
        return res

                
