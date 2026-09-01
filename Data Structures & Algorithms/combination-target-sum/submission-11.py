class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, path, remaining):
            # return all possible combination = target when start from nums[start], and historical path as path (not including current number)
            if remaining == 0:
                res.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                # choose
                # pruning:
                    if remaining - nums[i] < 0:
                        continue
                    path.append(nums[i])
                    # explore
                    dfs(i, path, remaining - nums[i])
                    #undo
                    path.pop()

        dfs(0, [], target)
        return res