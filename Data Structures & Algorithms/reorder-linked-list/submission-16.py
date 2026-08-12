# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find mid point
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        second_half_head = s.next
        s.next = None # first_half end with None, last node is s

        # 2. reverse secondhalf
        cur = second_half_head
        prev = None

        while cur:
            temp_cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_cur_next
        second_half_head = prev
        first_half_head = head
 

        # 3. merge
        while second_half_head:
            temp_first_next = first_half_head.next
            temp_second_next = second_half_head.next

            first_half_head.next = second_half_head
            second_half_head.next = temp_first_next
   

            first_half_head = temp_first_next
            second_half_head = temp_second_next
        return
