# Linked list contains nodes that connect one another.
# Each node has three attribute:
#   - key:  value stored in node
#   - prev: previous node
#   - next: next node
# Each linked list has one attribute 'head' which is a node.

class ListNode():
    def __init__(self):
        self.key = None
        self.prev = None
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def search(self, k):
        """ returns the first node with key = k. """
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x
    
    def insert(self, k):
        """ insert a node with key = k at the head of linked list. """
        x = ListNode()
        x.key = k
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x

    def delete(self, k):
        """ delete the first node with key = k. """
        x = self.search(k)
        # connect x.prev with x.next
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev
