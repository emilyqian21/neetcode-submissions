# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1: find the middle point(where fast pointer is at the end or out of range, then the position of slow pointer is the end of first half,
        #the position of the slow pointer.next is the start of the second half) of the linked-list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_half_start = head
        first_half_end = slow
     
        second_half_start = slow.next
        first_half_end.next = None
        curr = second_half_start
        prev = None

        # step 2: reverse the second half 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second_half_start = prev

        # step 3: merge
        while first_half_start and second_half_start:
            first_temp = first_half_start.next 
            second_temp = second_half_start.next

            first_half_start.next = second_half_start
            second_half_start.next = first_temp

            first_half_start = first_temp
            second_half_start = second_temp

            # time: O(N)
            # space: O(1) 
        
            



