class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        # kadane's algo
        #edge case 
        if not nums:
            return 0
        # main code
        cursum = nums[0]
        maxsum = nums[0]

        for n in nums[1:]:
            # greedy: either add it to current sum or start fresh
            cursum = max((cursum + n), n)
            maxsum = max(maxsum, cursum)
        return maxsum