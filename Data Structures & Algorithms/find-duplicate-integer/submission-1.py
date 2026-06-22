class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0 

        #round 1: to find the node that is in the cycle and 1 step away from the cycle start 
        while True:
            slow = nums[slow] #equivalent to slow.next
            fast = nums[nums[fast]] #equivalent to fast.next.next
            if slow == fast: # 当fast和slow相遇的时候，fast和slow指向的是离cycle start差一步的node
                break
        
        #round 2: to find the duplicate
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                break
    
        return slow

        # time: O(N)
        # space: O(1)