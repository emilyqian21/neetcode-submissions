class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # time: O( n * N^2) n --> copy的成本； N^2 一共的可能性
        # sapce:不算输出 O(n) --> stack, 算输出： O（n * N^2)
        res = []
        path = []
        def dfs(nums,start):
            # base case: when to stop exploring and record answer
            if start >= len(nums):
                res.append(path.copy())
                return
            
            # assume dfs works
            # current status is also a valid answer. 
            res.append(path.copy())

            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(nums, i + 1)
                #after adding it, pop
                path.pop()
        dfs(nums,0)
        return res
                
