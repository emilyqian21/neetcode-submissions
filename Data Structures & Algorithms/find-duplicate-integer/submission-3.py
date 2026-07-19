class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # linked list, cycle dectection, floyd's algo(fast and slow pointers)
        # fast = 0, slow = 0, fast走两步，fast和slow相遇的地方，是离cycle 起点X的位置
        # 再开启一个slow2 = 0, slow和slow2一起走，两者相遇的地方，就是cycle的起点 

        # time: O(n)
        # space: O(1)
        fast = 0 
        slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow