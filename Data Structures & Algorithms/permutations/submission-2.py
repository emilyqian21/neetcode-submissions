class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def dfs(path):
            #base case
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            #explore every options
            for i in range(len(nums)):
                #current node
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True
                else:
                    continue #skip this used value

                #explore other options from this path
                dfs(path)

                #cancel the choice
                path.pop()
                used[i] = False
        dfs([])
        return res
        #time: O(n!*n) 一共有n!个permutation，每个permutation 长度是len(nums) # space: O(n!*n)