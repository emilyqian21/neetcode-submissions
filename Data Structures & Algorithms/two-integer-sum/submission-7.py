class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key = number , val = index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i

        return [-1,-1]