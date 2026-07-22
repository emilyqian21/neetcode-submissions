class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # time: O(n × n!), 有 N！种可能，copy每个path的成本是n，因为path长度是n
        # space: auxiliary O(n) --> stack; O(n × n!) for output

        # Permutation 的核心：每一层都可以从所有数字里重新选择。 
        # 所以 dfs（start)不需要 start这个参数
        res = []
        path = []
        used = [False] * len(nums)
        def dfs():
            # base case 
            if len(path) >= len(nums):
                # valid answer
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                # if used, then skip
                if used[i] == True:
                    continue
                # choose the number
                path.append(nums[i])
                used[i] = True
                #continue the path 
                dfs() # 易错点，如果选了2 还能往前面选1 ，所以不能是dfs(i + 1)
                # undo
                path.pop()
                used[i] = False
        dfs()
        return res

