class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, path):
            # return all possible subsets start from nums[start]
            res.append(path.copy())
            for i in range(start, len(nums)):
                # choose
                path.append( nums[i])
                # explore
                dfs( i + 1, path)
                # undo
                path.pop()
        dfs(0, [])
        return res