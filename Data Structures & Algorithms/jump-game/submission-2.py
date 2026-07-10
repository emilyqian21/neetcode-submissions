class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # time: O(n)
        # space: O(1)
        n = len(nums)
        target = n - 1 # index, 最终我们要reach 0

        for i in range(n-1, -1, -1): #从后往前traverse
            max_jump = nums[i] # 在i可以跳最远的步数
            if i + max_jump >= target: #如果在i，可以达到target,那么新的target就是i,我们只要到达i就可以了，因为到达i后一定能到target
                target = i 
                            # 如果当前 i 不能到达 target，不代表更前面的 index 不可以。你应该继续往前找。
        return target == 0