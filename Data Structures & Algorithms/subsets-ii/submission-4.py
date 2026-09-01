class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start, path):

            res.append(path.copy())

            for i in range(start, len(nums)):
                # dedup
                if i > start and nums[i] == nums [i - 1]:
                    continue
                # choose
                path.append(nums[i])
                # explore
                dfs( i + 1, path)
                # undo
                path.pop()
            return
        
        dfs(0, [])
        return res