class Node:
    def __init__(self,key,val): # node with (val,key), with prev and next
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0,0) # left pointer to a dummy node
        self.right = Node(0,0) #right pointer to a dummy node
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {} # key = node.key, values = node

    def delete(self,node):
        #delete it from the double linked list （dict里的node是mutable的所以不用手动改，会自动更新，因为我们存的是那个node object本身）
        prev_temp = node.prev
        next_temp = node.next
        prev_temp.next = next_temp
        next_temp.prev = prev_temp  
    
    def insert(self,node):
        #insert it in the cache dict
        self.cache[node.key] = node
        #insert it as prev of right node
        prev_temp = self.right.prev
        self.right.prev = node
        node.prev = prev_temp
        prev_temp.next = node
        node.next = self.right
        
    def get(self, key: int) -> int:
        # get the node: 1) check if there is match, if not return -1 2)if there's match, return it and delete current and insert new right before right node
        if key not in self.cache:
            return -1
        else:
            res = self.cache[key].val #node.val
            # delete it from  the double linked list
            self.delete(self.cache[key]) #delete the node
            # add it as right.prev in double linked list
            self.insert(Node(key,res))
            #return res 
            return res

    def put(self, key: int, value: int) -> None:
        # put the node: 1)if there is match, delete the current one and insert 2) if there is no match, just insert 3)over capacity, delete the left.next
        # case 1: if there's match, delete current one and insert new one 
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(Node(key,value))
        # case 2: if there's no match, insert new one
        else:
            self.insert(Node(key,value))

        # case 3: if over capacity, delete the left.next in the double linked list and the cache. the delete function only delete in the double linked list
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
        # time: O(1), linked list 删除 get都是 O（1），但如果用array的话因为需要移动element，所以是O（N）
        # space: O(n)
