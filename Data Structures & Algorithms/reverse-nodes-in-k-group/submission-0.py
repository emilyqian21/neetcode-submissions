# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 4步：1）找每一组的Kth元素 2）如果没有kth 说明已经到底了，直接return 3)reverse 4) reconnect
        dummy = ListNode(None, head)
        groupprev = dummy
        # step 1:找每一组的kth元素
        while True:
            kth = groupprev 

            for i in range(k):
                kth = kth.next
            # step 2: 如果没有kth,说明到底了，直接return
                if not kth: #易错点：还在每个for 里面检查，因为下一步是需要keth.next的
                    return dummy.next
            
            # step 3: reverse
            groupnext = kth.next
            prev = groupnext # prev就是这个new list的最后node指向的node
            cur = groupprev.next

            while cur != groupnext:
                temp_next = cur.next
                cur.next = prev
                prev = cur
                cur = temp_next

            # step 4: reconnect
            #之前：groupprev -> 1 -> 2 -> 3 -> groupnext
            # reverse 后： groupprev ->  1
                             #          |
                             #      3-> 2
            #需要变成：groupprev -> 3 -> 2 -> 1 -> groupnext
            oldhead = groupprev.next
            groupprev.next = kth
            oldhead.next = groupnext
            # move to next group
            groupprev = oldhead
            

