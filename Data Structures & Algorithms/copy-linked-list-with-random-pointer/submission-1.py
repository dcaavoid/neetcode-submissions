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
        # In deep copy, through iteration, since random pointers might point to a node that haven't created yet,
        # use two passes with hash map(for O(1) retrival):
        # First pass: create each new node, and use old node as key and new node as its value;
        # Second pass: link the next pointer through the next pointer in the old linked list, 
        #              and link the random pointer through the hash map.
        oldToCopy = {None: None}
        curr = head

        # First pass: create new nodes and map old nodes to new nodes
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass: link .next and .random
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
