# O(1) for get and put -> hash map: key = key, value = node(key, value)
# Doubly linked list
class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: node(key, val)
        self.left = Node(0, 0)  # least recently used pointer
        self.right = Node(0, 0) # most recently used pointer
        self.left.next = self.right
        self.right.prev = self.left

    # Remove from the list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert to the most recently used
    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update this node to most recenlty used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # If the key exists, remove from current linked list
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Remove the least recently used node if exceeds capacity.
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
