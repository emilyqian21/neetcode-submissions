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
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # 左边有序
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # 右边有序
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1