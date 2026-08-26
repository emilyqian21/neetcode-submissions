class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start from where n-1 doesn't exist
        max_len = 0
        numset = set(nums)

        for num in nums:
            if (num - 1) in numset:
                continue
            start = num
            length = 1
            while start + 1 in numset:
                length += 1
                start  += 1
            max_len = max(max_len, length)
        return max_len