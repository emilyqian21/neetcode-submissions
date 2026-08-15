class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, path, pathsum):
            # when to record
            if pathsum == target:
                res.append(path.copy())
                return 
            
            # main logic
            # choice opitons
            for i in range(start, len(nums)):
                # pruning
                if nums[i] + pathsum > target:
                    break # no need to continue this for loop

                # make choice
                path.append(nums[i])

                # explore
                dfs(i, path, pathsum + nums[i]) # reuse the same number

                # undo
                path.pop()
            
            return 

        dfs(0,[],0)
        return res