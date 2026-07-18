# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers with set distance
        # time: O(n)
        # space: O(1)
        dummy = ListNode(None)
        dummy.next = head

        l = dummy
        r = head

        # 让r - l 保持 n 
        while n > 0 and r:
            r = r.next
            n -= 1
        
        # 当while结束的时候，就是r走到尽头的时候，l此刻就在要删掉的元素前面一格
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next

        return dummy.next 