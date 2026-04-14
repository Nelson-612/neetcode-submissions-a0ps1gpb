class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.map = {}
        self.capacity = capacity
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev =node.prev
    
    def insert(self, node):
        next = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self.insert(node)
        if len(self.map) > self.capacity:
            lru = self.dummy_tail.prev
            self.remove(lru)
            del self.map[lru.key]
