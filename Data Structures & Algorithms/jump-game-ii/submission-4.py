class Solution:
    def jump(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        # find the farthest position for each jump 
        l = 0 
        r = 0 
        farthest = 0
        step = 0 
        while r < len(nums) - 1: # while r is left of the last element, we continue the algo
            for i in range(l,r + 1):
                farthest = max(farthest, i + nums[i])
            step += 1
            l = r + 1
            r = farthest

        return step
            