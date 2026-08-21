class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        def dfs(start, path, pathsum):
        # dfs(start, path, pathsum) means traverse all possible combinations of nums in nums[start:], record the historical number in path (not include current number), pathsum not include current number as well
        #base case: when to record 
            if pathsum == target:
                res.append(path.copy())
                return
            
            # main logic
            for i in range(start, len(candidates)):
                # make choice
                if i > start and candidates[i] == candidates[i - 1]: # duplicate
                    continue
                # pruning
                if pathsum + candidates[i] > target:
                    break # no need to further explore in this for loop
                path.append(candidates[i])
                dfs(i + 1, path, pathsum + candidates[i]) # use i + 1 bc cant use same element again
                path.pop()
            return 

        dfs(0, [], 0)
        return res