# For doubly linked list
class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}   # key to a pointer to the Node(key, val)
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # Remove the node from the linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    

    # Insert the node from the linked list (most right)
    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            # Remove the existing node from the linked list
            self.remove(self.cache[key])

            # Insert the existing node to the most right of the linked list
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1        


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the existing node from the linked list
            self.remove(self.cache[key])
        
        # Insert the node to the most right of the linked list
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If exceeds capacity, remove lru from both the linked list and the hash map
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del (self.cache[lru.key])
        
        
