class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # main logic:  遍历到每个位置时，维护“目前最远能到哪里”，如果 i > farthest，说明当前这个位置都到不了
        # main definition: farthest = 目前最远能到达的位置
        farthest = 0
        for i in range(len(nums)):
            if i > farthest: # unreachable
                return False
            farthest = max(farthest, nums[i] + i)
        return True