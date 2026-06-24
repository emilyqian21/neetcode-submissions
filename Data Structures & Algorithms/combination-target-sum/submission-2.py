class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # res = []
        # nums.sort()

        # def dfs(start, remaining, path):
        #     # record results if necessary --> when necessary? --> when remaining == 0
        #     if remaining == 0:
        #         res.append(path.copy())
        #         return 
            
        #     #recursive
        #     for i in range(start,len(nums)): # all choices, if start = 0, len(nums) = 4, i = 0,1,2,3
        #         #pruning 
        #         if nums[i] > remaining:
        #             break

        #         #choose
        #         path.append(nums[i])
                
        #         #keep searching based on current path
        #         dfs(i, remaining - nums[i], path) # start = i, not i+1 because we're allowed to use the nums[i] again 

        #         #undo the choice
        #         path.pop()

        # dfs(0,target,[])
        # return res


        #path sum version
        res = []
        nums.sort()

        def dfs(start, current_sum, path):
            if current_sum == target:
                res.append(path[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(nums)):
                # optional pruning (works because sorted)
                if current_sum + nums[i] > target:
                    break

                path.append(nums[i])
                dfs(i, current_sum + nums[i], path)
                path.pop()

        dfs(0, 0, [])
        return res