class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
                # main logic: 
        # example [1,2,3,4,5,6,7] k = 3
        # 1. reverse the whole array [7,6,5,4,3,2,1]
        # 2. reverse the first k elements [5,6,7,4,3,2,1]
        # 3. reverse the remaining elements [5,6,7,1,2,3,4]
        # 4. don't forget the normalize k, if k > len(nums), k = nums % k

        def reverse(l, r): # reverse the nums[l: r + 1]
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k %= len(nums)
        # 1. reverse the whole array
        reverse(0, len(nums) - 1)
        # 2.reverse the first k element
        reverse(0, k - 1)
        # 3. reverse the remaining element
        reverse(k, len(nums) - 1)

