# stack: LIFO (last in first out) data structure.
class Stack():
    def __init__(self, height):
        # stack top stores the NEXT empty position in stack
        self.top = 0
        self.start = 0
        self.height = height
        self.stack = [None for _ in range(height)]
    
    def is_empty(self):
        """ check if stack is empty; if empty, return True """
        return self.top == self.start
    
    def underflow(self):
        """ check stack underflow condition """
        return self.top < self.start
    
    def overflow(self):
        """ check stack overflow condition """
        return self.top == self.height
    
    def push(self, element):
        """ push one element to stack and return it; if overflow, return None """
        # check overflow
        if self.overflow():
            return None

        # push element and increment stack top
        self.stack[self.top] = element
        self.top = self.top + 1
        
        return element
    
    def pop(self):
        """
            pop one element from stack and return it; if underflow, return None
            pop does not alter the items of stack; it alters the pointer.
        """
        # decrement stack top and check underflow
        self.top = self.top - 1
        if self.underflow():
            return None
        
        # pop element
        return self.stack[self.top]

# queue: FIFO (first in first out) data structure.
class Queue():
    def __init__(self, length):
        self.queue = [None for _ in range(length)]
        self.length = length
        self.head = 0
        self.tail = 0
        
        # since overflow and underflow both happens after head == tail, we 
        # need another flag indicating whether it's overflow or underflow
        self.full = 0
    
    def is_empty(self):
        """ check if queue is empty; if empty, return True """
        return (self.head == self.tail and self.full == 0)
    
    def enqueue(self, element):
        """ add an element to queue and return that element. if full, return None """
        if self.full == 1:
            return None

        # add element and increment tail
        self.queue[self.tail] = element
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail = self.tail + 1

        # check overflow condition
        if self.tail == self.head:
            self.full = 1
        
        return element
    
    def dequeue(self):
        """ remove an element from queue and return that element. if empty, return None """
        if self.is_empty():
            return None

        # clear full flag
        self.full = 0

        # increment head and return element
        element = self.queue[self.head]
        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head = self.head + 1
        
        return element
