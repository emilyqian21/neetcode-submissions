class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort() # 易错点：我们要先[1,1,2]排序，这样下面才能去重

       
        def dfs(start):  #[1,2,1] [1,1,2]，[2,1,1] 算一类
            if start == len(nums):
                # if valid 
                res.append(path.copy())
                return 
            
            # current path is also valid
            res.append(path.copy())

            for i in range(start, len(nums)):
                # make choice
                # if used[i] == True:
                if i > start and nums[i]== nums[i-1]: #因为 Subsets II 的去重规则是：同一层（same recursion level）不能选择相同数字。
                    continue
                path.append(nums[i])

                #continue this path
                dfs( i + 1)
                # undo
                path.pop()

        dfs(0)
        return res