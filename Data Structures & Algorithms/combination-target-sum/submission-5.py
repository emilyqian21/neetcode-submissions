class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, pathsum, path):
            # when to return 
            if pathsum == target:
                # find the answer     
                res.append(path.copy())
                return
            
            # main logic
            for i in range(start, len(nums)):       
                if nums[i] + pathsum > target:
                    break

                # explore 
                path.append(nums[i])    
                dfs(i, pathsum + nums[i], path)

                # undo
                path.pop() # 用pop，不要用remove(nums[i])
            return 
        
        dfs(0,0,[])
        return res