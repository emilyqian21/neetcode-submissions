class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        prefix_prod = 1
        suffix = [1]*len(nums)
        suffix_prod = 1
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = prefix_prod
            else:
                prefix_prod *= nums[i-1]
                prefix[i] = prefix_prod

        for i in range(len(nums)-1, -1,-1):
            if i == len(nums)-1:
                suffix[i] = suffix_prod
            else:
                suffix_prod *= nums[i+1]
                suffix[i] = suffix_prod
        return [  x*y for x, y in zip(prefix,suffix)]