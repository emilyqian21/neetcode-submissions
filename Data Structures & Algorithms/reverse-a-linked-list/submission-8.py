# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        4 steps:
        Save
        Reverse
        Advance prev
        Advance curr"""
        # time: O(n)
        # space: O(1)
        cur = head
        prev = None
        while cur:
            temp_next = cur.next # save
            cur.next = prev # reverse

            prev = cur # advance prev
            cur = temp_next # advance cur
            

        return prev
                       