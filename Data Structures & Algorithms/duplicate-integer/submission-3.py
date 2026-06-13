class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
#         return not len(set(nums)) == len(nums)

# #TIME: o(n)
# #SPACE: o(n)
        return not len(set(nums)) == len(nums)
        #time: o(n)
        #space: o(n)