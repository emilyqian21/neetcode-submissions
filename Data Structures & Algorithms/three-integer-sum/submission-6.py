class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # pattern:
        # solution:

        # time:
        # space:

        # 因为 i,j,k 是distinct, 而且不能有duplicate， 所以扫描一遍就可以



        nums.sort()
        res = []

        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break

            target = -nums[i]

            l = i + 1
            r = len(nums)-1

            while l < r:

                curr = nums[l] + nums[r]

                if curr == target:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif curr < target:
                    l += 1

                else:
                    r -= 1

        return res

