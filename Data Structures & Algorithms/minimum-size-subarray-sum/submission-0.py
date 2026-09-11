class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # main logic:
        # 1. expand right until window is valid: sum >= target
        # 2. while valid, shrink left as much as possible
        # 3. record the minimum window length

        l = 0
        min_res = float('inf')
        window_sum = 0

        for r in range(len(nums)):
                window_sum += nums[r]

                while window_sum >= target:
                    min_res = min(min_res, r - l + 1)

                    # contract the window from the left
                    window_sum -= nums[l]
                    l += 1

        return 0 if min_res == float('inf') else min_res