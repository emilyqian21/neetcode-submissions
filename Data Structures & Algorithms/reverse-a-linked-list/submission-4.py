# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# solution:iterative, three pointers, cur, pre, cur_next_temp
        cur = head
        pre = None

        while cur:
            cur_next_temp = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next_temp #在斩断任何一条原有的 .next 连线之前，必须先用一个临时变量（如 temp 或 prev）把即将断开的那一头死死拽住。
        return pre
        #time: O(N)
        #space: O(1)
                

# solution: recursive        
#         if not head or not head.next:
#             return head

#         newhead = self.reverseList(head.next)  #
#         head.next.next = head
#         head.next = None

#         return newhead
#         # time: O(N)
#         # space: O（N）,虽然指针是O(1)但是有 recursive call stack， call stack是 O (N)
# ## Recursive Reverse Linked List
# # 永远只是在修改指针，只有一个linked list，不会创建copy
# # 每个node存两个variable,一个是value，一个是下一个连接的点，比如 1->2->3，当head 指向1, 进行了rseverselist(head.next)后， new head--> 3-->2-->None, 
# #但是 对于node 1来说，它存的value是1，指的下一个还是2，所以 就变成了
# #  3 -> 2 -> None
# #      ^
# #      |
# # 1 ----

