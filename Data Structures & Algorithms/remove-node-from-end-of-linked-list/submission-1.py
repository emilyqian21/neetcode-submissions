# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        l = dummy
        r = head
        while n > 0 and r:
            r = r.next
            n -= 1
        while r:
            l = l.next
            r = r.next 

        l.next = l.next.next

        return dummy.next
        # time: O(N)
        # space: O(1)
        #问题:如何从最后往前数第N个node ? --> 利用two pointers, left and right, 两者距离保持N，同时前进一步，当right 变成none的时候，L指的就是从后往前数第N个；
        #但是因为要删除L指向的node，我们需要L之前的元素，所有我们可以把L一开始设置在dummy上，right设置在head，然后让L和R之间的距离变成N+1，这样当right变成none的时候，
        # L指向的是要删除的node之前的node,就可以用 l.next = l.next.next来删除了，最后直接return dummy.next