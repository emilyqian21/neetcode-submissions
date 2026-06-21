# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head

        while f and f.next: # 当没有cycle的话，fast指针一定先触底，那么f 和f.next就会没有
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
        #time: O(N)
        #space: O(1)
