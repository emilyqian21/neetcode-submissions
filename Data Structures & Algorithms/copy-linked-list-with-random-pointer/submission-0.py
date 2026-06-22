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
        oldtonew = {None:None} #key is old node, #val is new node
        

        #first pass, to create nodes with vals
        cur = head
        while cur:
            oldtonew[cur] = Node(cur.val)
            cur = cur.next
        
        #second pass, to create pointers, both next and random pointers
        cur = head
        while cur:
            oldtonew[cur].next = oldtonew[cur.next]
            oldtonew[cur].random = oldtonew[cur.random]
            cur = cur.next
        
        return oldtonew[head]