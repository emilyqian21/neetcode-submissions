class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # time: O (n^3) there're at most n^2 subarray, and we run n for each of the subarray
        # sapce o (n^2) there are at most n^2 subarray(O(n²) possible intervals (l, r).)

        # top down:
        # dfs definition: 
        #               dfs(l, r) --> # max coins from bursting ALL balloons in nums[l:r+1]
        # main logic:
        #              假设 i 是 [l, r] 里最后一个被戳的 balloon
        #               那么总 coins = 在当前区间 [l, r] 里，按照“最后戳 i”这个方案，把所有 balloon 都戳完以  后，能拿到的 coins 总和
        #                           = 先把 i 左边全部戳掉 + 先把 i 右边全部戳掉 + 最后戳 i


        nums = [1] + nums + [1] # add 1 both before and after the nums
        memo = {} # save (l,r) max coins

        def dfs(l,r):
            # max coins from bursting ALL balloons in nums[l:r+1]
            # base case
            if l > r:
                return 0 
            if (l,r) in memo:
                return memo[(l,r)]
            
            # process the cur node
            max_coins = 0
            for i in range(l, r + 1): # 每个i都可能是最后一个被戳破的气球
                left_coins = dfs(l, i - 1)
                right_coins = dfs(i + 1, r)
                coins = left_coins+ (nums[l - 1] * nums[i] * nums[ r + 1]) + right_coins # we pop i last, so 1[i]1, l-1 ->1  r - 1> 1

                max_coins = max(max_coins, coins) # dfs(l, r) needs to remember the best answer among all possible choices of i
            memo[(l,r)] = max_coins
                
            return memo[(l,r)]
        
        return dfs(1, len(nums) - 2) # 因为我们一开始加了两个boundry 1 


        # nums = [1] + nums + [1]
        # nums = [3, 1, 5, 8]
        # index:  0  1  2  3  4  5
        # nums:  [1, 3, 1, 5, 8, 1]
        #          ↑              ↑
        #       boundary       boundary