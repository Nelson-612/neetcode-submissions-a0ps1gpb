class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev= None

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev = self.right.prev
        next = prev.next
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        else:
            node = self.hash_map[key]
            self.remove(node)
            self.insert(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.hash_map[key] = node
            self.insert(node)
            if len(self.hash_map) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.hash_map[lru.key]
            
