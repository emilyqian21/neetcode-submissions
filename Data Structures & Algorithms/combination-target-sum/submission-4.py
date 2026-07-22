class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Time: O(n ^(T/M)),where n is the number of candidates and M is the smallest candidate, because we explore all possible combinations up to depth T/M.
        # Space:
            # auxiliary: O(T/M) for the recursion stack and the current path, excluding the output.
            # output: O( K * T/M), 答案数量为 K，每个组合长度最多 T/M
        res = []
        path = []

        def dfs(start,pathsum):
            # 易错点：valid的时候才记录答案
            if pathsum == target:
                res.append(path.copy())
                return
            #base case
            if start == len(nums):
                return
            
            # explore possibilities in this path
            for i in range(start, len(nums)):
                if target - pathsum >= nums[i]:
                    # choose this number
                    path.append(nums[i])
                    #else continue
                else:
                    continue
                # continue exploring the path
                dfs(i, pathsum + nums[i]) # 在这里update pathsum， 就不用在pop后改了；# because we can reuse the elements, so start from i again
                path.pop()
        dfs(0,0)
        return res
