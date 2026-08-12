# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the mid point(first part length >= second part length)
        s = head
        f = head.next 
        while f and f.next:
            s = s.next
            f = f.next.next
        second_head = s.next
        s.next = None # first half end at s
        #head is the first head
        first_head = head
       

        # 2. reverse the second part
        cur = second_head
        prev = None
        while cur:
            temp_cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_cur_next  # error point 
        # prev is the second head
        second_head = prev
       

        # 3. merge first and second part, return dummy.next
        while second_head: # 把second head 插在first head 和first head.next 之间
            first_next = first_head.next
            second_next = second_head.next # 因为之后会改变next的node,所以先记录一个temp

            first_head.next = second_head
            second_head.next = first_next

            first_head = first_next
            second_head = second_next





