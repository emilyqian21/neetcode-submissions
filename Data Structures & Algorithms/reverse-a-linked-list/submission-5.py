# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        a = None
        while cur :
            temp_next = cur.next
            cur.next = a
            a = cur
            cur = temp_next       

        return a
                       