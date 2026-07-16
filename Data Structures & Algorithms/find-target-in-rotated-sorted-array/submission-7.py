class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        每一轮都做两件事：

        1.判断哪一半是有序的。
        2.判断 target 是否落在这个有序区间内。
            在 → 去这一半。
            不在 → 去另一半。
        不要根据 nums[m] 和 target 的大小直接决定方向，因为整个数组并不是全局有序的。
        这个思维模板也是很多旋转数组二分题（如找最小值、搜索目标等）的核心。
        """
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2

            if nums[m] == target:
                return m
            
            if nums[m] > nums[r]: # in left sorted part 
                if nums[l] <= target < nums[m]: # target between l and m 
                    # search this space
                    r = m - 1
                else: # target larger than m 
                    l = m + 1

            else: # in right sorted part
                if nums[m] < target <= nums[r]: # target between m and r
                    l = m + 1
                else: # target smaller than m, not in m and r
                    r = m - 1
        return -1 
