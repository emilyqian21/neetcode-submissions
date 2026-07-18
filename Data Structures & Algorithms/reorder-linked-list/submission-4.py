# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 3 步走 ：
        #   1）找mid point(前半段>= 后半段，当奇数时前半段更长，偶数时一样长) 
        #   2）reverse 第二段
        #   3） merge第一、第二段

        # time: O(n)
        # space: O(1)

        # find mid point
        f = head.next
        s = head

        while f and f.next:
            f = f.next.next
            s = s.next
        first = head
        second = s.next 
        s.next = None # first : head --> s --> none # second: s.next ---> None

        # reverse second
        prev = None
        cur = second
        while cur:
            temp_next = cur.next 
            cur.next = prev
            prev = cur
            cur = temp_next
        second = prev # 需要update seconds，注意是prev!
        
        # merge
        # the head must from the first part
  
        while second:
            temp_first_next = first.next
            first.next = second
            first = temp_first_next

            temp_second_next = second.next
            second.next = temp_first_next
            second = temp_second_next

        return 
            