class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 【初始化】大家都从起点（下标 0）出发
        # 注意：这里不能初始化为 slow = 0, fast = 0，因为 while 循环会直接进不去。
        # 所以我们直接在第一步把它们推到下一站。
        slow = nums[0]         # 相当于 slow = slow.next
        fast = nums[nums[0]]   # 相当于 fast = fast.next.next

        # ---- 第一阶段：快慢指针追赶，寻找“相遇点”（在这题里是 Node 4） ----
        while slow != fast:
            slow = nums[slow]        # 慢指针走 1 步：slow = slow.next
            fast = nums[nums[fast]]  # 快指针走 2 步：fast = fast.next.next

        # ---- 第二阶段：寻找“环的入口”（在这题里是 Node 2） ----
        # 此时 slow 停在 Node 4，我们将 fast 扔回大后方的起点（下标 0）
        fast = 0
        
        # 大家都用相同的速度（每次 1 步）往前走
        while slow != fast:
            slow = nums[slow]  # 慢指针走 1 步
            fast = nums[fast]  # 快指针也走 1 步

        # 当它们再次相遇时，停下来的地方就是环的入口（Node 2）
        # 此时 slow 和 fast 的值都是 2，这个“下标值”就是我们要找的重复数字
        return slow