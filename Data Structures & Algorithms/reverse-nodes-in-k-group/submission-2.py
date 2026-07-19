# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       # time: O(n)
       # space: O(1)
       #Time complexity is O(n) because each node is visited a constant number of times during finding kth nodes, reversing groups, and reconnecting. Space complexity is O(1) because we only use constant extra pointers and do the reversal in-place.
        # 4步：
        # 1）找到每一组的第 k 个节点（kth）
        # 2）如果不存在 kth，说明剩余节点不足 k 个，保持原样，直接 return
        # 3）reverse 当前 group
        # 4）reconnect，把反转后的 group 接回原链表


        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # step 1: 找当前 group 的 kth 节点
            # group_prev 是当前 group 前面的节点
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                # 易错点：
                # 必须在这里检查 kth 是否存在，
                # 因为下一步需要使用 kth.next
                if not kth:
                    return dummy.next

            # step 3: reverse 当前 group
            # 原链表：
            # group_prev -> 1 -> 2 -> 3 -> group_next
            #
            # reverse 后：
            # group_prev -> 3 -> 2 -> 1 -> group_next

            group_next = kth.next

            # prev 是反转后当前 group 的 tail 要连接的节点
            # 因为反转后：
            # 1 会变成 tail，需要指向 group_next
            prev = group_next

            cur = group_prev.next

            while cur != group_next:
                temp_next = cur.next

                cur.next = prev
                prev = cur
                cur = temp_next

            # step 4: reconnect
            # reverse 前：
            # group_prev -> 1 -> 2 -> 3 -> group_next
            #
            # reverse 后：
            # group_prev -> 1 -> group_next
            #              ↑
            #          3 -> 2 -> 1
            #
            # 需要重新连接：
            # group_prev -> 3 -> 2 -> 1 -> group_next

            old_head = group_prev.next  # 原来的 head，reverse 后变成 tail

            group_prev.next = kth       # 接到 reverse 后的新 head
            old_head.next = group_next  # tail 接回下一组

            # move to next group
            # 下一轮从当前 group 的 tail 开始找 kth
            group_prev = old_head