"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #交织链表 Interleaving Method or In-place Clone Time O(N) Space O(1)
        if not head:
            return None
        
        # Step 1: 在每个原节点后面强行插入一个克隆节点
        curr = head
        while curr:
            nxt = curr.next
            clone = Node(curr.val)
            curr.next = clone
            clone.next = nxt
            curr = nxt
            
        # Step 2: 顺藤摸瓜，连接新节点的 random 指针
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next # 连跳两步，只走原节点
            
        # Step 3: 拆分交织的链表（你最擅长的双指针分离）
        curr = head
        dummy = Node(0)
        clone_curr = dummy
        
        while curr:
            nxt = curr.next.next # 记录原链表的下一个
            
            # 把克隆节点提取出来挂在新链表上
            clone_curr.next = curr.next
            clone_curr = clone_curr.next
            
            # 恢复原链表的指向
            curr.next = nxt
            curr = nxt
            
        return dummy.next




        # #solution : Hashmap Time O(n) Space O(1)
        # oldtonew = {None:None} #key is old node, #val is new node
    
        # #first pass, to create nodes with vals
        # cur = head
        # while cur:
        #     oldtonew[cur] = Node(cur.val)
        #     cur = cur.next
        
        # #second pass, to create pointers, both next and random pointers
        # cur = head
        # while cur:
        #     oldtonew[cur].next = oldtonew[cur.next]
        #     oldtonew[cur].random = oldtonew[cur.random]
        #     cur = cur.next
        
        # return oldtonew[head]

        # #time: O(N)
        # #space: O(N)