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
        # two passes
        # first pass to create the copy nodes （no links yet! )
        # second pass to create the links

        # time: O(n)
        # space: o(n)
        cur = head
        old2copy = {None:None}
        #first pass
        while cur:
            old2copy[cur] = Node(cur.val) # create a copy of current node
            cur = cur.next # update the cur

        #second pass 
        cur = head
        while cur:
            old2copy[cur].next = old2copy[cur.next]
            old2copy[cur].random = old2copy[cur.random]
            cur = cur.next

        #finish two passes
        return old2copy[head]




