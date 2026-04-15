class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.dummy_head = Node(0,0)
        self.dummy_tail = Node(0,0)
        self.capacity = capacity
        self.map= {}
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        node.prev = self.dummy_tail.prev
        node.next = self.dummy_tail
        self.dummy_tail.prev.next = node
        self.dummy_tail.prev= node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            del self.map[key]

        node = Node(key, value)
        self.insert(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            lru = self.dummy_head.next
            self.remove(lru)
            del self.map[lru.key]