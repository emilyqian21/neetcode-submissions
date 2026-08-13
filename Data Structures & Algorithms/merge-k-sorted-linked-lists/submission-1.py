# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] # (node.val, index of list to represent the listnode, listnode)

        # save the linkedlist into the heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        # merge
        dummy = ListNode(None)
        cur = dummy

        while heap:
            #pop 
            _, i, cur_linked_list = heapq.heappop(heap)
            
            # merge into dummy
            cur.next = cur_linked_list
            cur = cur.next

            #update curlinkedlist and add back to heap 
            if cur_linked_list.next:
                heapq.heappush(heap, (cur_linked_list.next.val, i, cur_linked_list.next))

        return dummy.next 
