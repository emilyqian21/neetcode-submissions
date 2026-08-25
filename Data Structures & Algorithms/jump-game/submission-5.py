class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest: # unreachable
                return False
            farthest = max(farthest, nums[i] + i)
        return True