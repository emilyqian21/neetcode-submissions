class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, path, pathsum):
            # traverse from nums[start:] with path and pathsum, when pathsum <= target
            # no need to return, traverse
            # when to record the answer
            if pathsum == target:
                res.append(path.copy())
                return
            
            # main logic
            # make choice
            for i in range(start, len(nums)):
                if pathsum + nums[i] > target:
                    break
                path.append(nums[i])

                 # explore recursively
                dfs(i, path, pathsum + nums[i])

                # undo
                path.pop()
                
            return 
        
        dfs(0,[],0)
        return res
               