# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. find kth
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # 2. boundaries
            group_next = kth.next
            cur = group_prev.next
            prev = group_next

            # 3. reverse group
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 4. reconnect + move
            old_head = group_prev.next
            group_prev.next = kth
            group_prev = old_head