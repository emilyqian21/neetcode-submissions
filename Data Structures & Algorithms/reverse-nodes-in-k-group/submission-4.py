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
                    return dummy.next # # 剩下不足 k 个，不反转，结束，直接return 答案

            # 2. boundaries
            group_next = kth.next
            cur = group_prev.next
            prev = group_next  # 把reverse后的part的尾巴连到下一个part的开头
 
            # 3. reverse group
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 4. reconnect + move
            old_head = group_prev.next  # 保存旧 head，因为它会变成 tail
            group_prev.next = kth  # 前面接到新的 head
            group_prev = old_head # tail 变成下一组的 group_prev

            #reverse 前：
            # group_prev -> A -> B -> C -> next
            #               ↑         ↑
            #            old_head    kth


            # reverse 后：
            # group_prev    C -> B -> A -> next
            #               ↑         ↑
            #              kth     old_head

            # 然后 group_prev.next = kth
            # 得到 group_prev -> C -> B -> A -> next
            
            # 最后 group_prev = old_head
            # 就是                      group_prev
                    #                        ↓
                    # ... -> C -> B -> A -> next