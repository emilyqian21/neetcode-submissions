# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap里存（node.val, i, node)， 每次pop完就push下一个节点
        # step 1: 存heap
        heap = []
    
        for i, linked_list in enumerate(lists):
            # 易错点：要检查linked_list是否存在
            if linked_list:
                heapq.heappush(heap, (linked_list.val, i, linked_list))
        # step 2: merge 
        dummy = ListNode(None)
        cur = dummy
        while heap:
          _,i,linked_list =  heapq.heappop(heap)
          cur.next = linked_list
          linked_list = linked_list.next
          #易错点：没有move cur
          cur = cur.next
          # push next node 
          if linked_list:
            heapq.heappush(heap, (linked_list.val, i, linked_list))
        return dummy.next
