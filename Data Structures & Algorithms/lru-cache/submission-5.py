# time
#    Hash map：通过 key 快速找到 node。

#   Doubly linked list：快速删除和插入 node。

#   所以 get / put 都是 O(1)。

# space:
    #空间就是 capacity 个 node, O(n)


class ListNode:
    def __init__(self, val, key, prev, nxt):
        self.val = val
        self.key = key #易错点：这里的key不是val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.left = ListNode(None, None, None, None)
        self.right = ListNode(None,None,self.left,None)
        self.left.nxt = self.right 
        self.cap = capacity
        #hashmap
        self.cache = {} # key: nodes
    
    def delete(self,node):
        # delete from double linked list
        temp_prev = node.prev
        temp_next = node.nxt
        temp_prev.nxt = temp_next
        temp_next.prev = temp_prev

        # delete from hashmap
        del self.cache[node.key]

    def insert_right (self,node):
        # insert in the double linked list
        right = self.right
        temp_prev = self.right.prev
        temp_prev.nxt = node
        node.nxt = right
        right.prev = node
        node.prev = temp_prev

        # insert in the hashmap
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        # 1. get the node 
        if key in self.cache:
            node = self.cache[key]
            
            # 2. update in the double linked list to be rightmost
            self.delete(node)
            self.insert_right(node)

            return node.val# 易错点: return之后的代码就不会运行 所以要放在 delete和insert_right之后
        else:
            return -1
      

        

    def put(self, key: int, value: int) -> None:
        # if already in the cache, delete it first
        if key in self.cache:
            self.delete(self.cache[key])
        # insert from right
        node = ListNode(value, key,None, None)
        self.insert_right(node)
        # if the len(cache) > capacity, need to delete
        while len(self.cache) > self.cap:
            lru = self.left.nxt
            self.delete(lru)
        
