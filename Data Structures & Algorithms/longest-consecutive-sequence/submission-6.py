class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start from where n-1 doesn't exist
        max_len = 0
        exist = set(nums)

        for i in range(len(nums)):
            if nums[i] - 1 in exist:
                continue
            start = nums[i]
            count = 1
            while start + 1 in exist:
                count += 1
                start += 1
           
            max_len = max(max_len, count)
        return max_len
