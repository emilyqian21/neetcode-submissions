class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, used):

            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                # choose
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                # explore
                dfs(path, used)
                # undo
                path.pop()
                used.remove(nums[i])
            return
        dfs([], set())
        return res