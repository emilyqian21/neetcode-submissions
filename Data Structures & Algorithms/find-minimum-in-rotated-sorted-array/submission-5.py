class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r)//2


            if nums[m] > nums[r]:
                # m 在左边的大数部分
                # minimum 一定在 m 右边
                l = m + 1
            else:
                # m 在右边的小数部分
                # m 自己可能就是 minimum
                r = m

        return nums[l]
