# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None) #res是指针！！！！！
        dummy = res
        # node(None)  -->  None
        #     ^             ^
        #     |             |
        #    res,dummy    dummy.next

        l = list1
        r = list2

        while l and r:
            if l.val < r.val:
                res.next = l
                l = l.next
                res = res.next
            else:
                res.next = r
                r = r.next
                res = res.next
        if l:
            res.next = l
        else:
            res.next = r

        return dummy.next
        #time: O (length of list 1 and lenght of list 2)
        #space: O(1)

