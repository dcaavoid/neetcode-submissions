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
        # Use hash map: key: old node, value: new node
        # First iterate through each old node and map to new node
        # How to resolve the new nodes' next and random mapping
        # 3  7  4  5
        # 3  7  4  5
        # Create the hash map None: None to resolve when head = None
        oldToNew = {None: None}   # key: old node; value: new node
        curr = head

        # First create the old to new mapping
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        # Then build the .next and .random fro the new node
        curr = head
        while curr:
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next
        
        return oldToNew[head]