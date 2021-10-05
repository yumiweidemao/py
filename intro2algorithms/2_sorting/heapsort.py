# Heap is a data structure. Any heap A has two main attributes:
#   A.length is the number of elements in the container.
#   A.heap_size is the number of elements in the heap.

# Given a position i of an element in a heap, we can calculate:
# PARENT(i) = i/2;
# LEFT(i) = 2i;
# RIGHT(i) = 2i + 1;
# Note that in Python/C++, the starting index is zero, so the formulas will change.

# Max heap & Min heap:
# Max heap: any element is not larger than its parents.
# Min heap: any element is not smaller than its parents.

# The height of a heap of n elements is lg(n).

# Python has a library for heap.
# >>> import heapq
# >>> help(heapq)

# Since we need the attribute heap_size, create a new class that extends from List.

class Heap(list):
    def __init__(self, A):

        super().__init__(A)
        self.heap_size = len(A)

def parent(i):
    """ Calculate parent index """
    if i == 0:
        return None
    return (i+1)//2 - 1

def left(i):
    """ Calculate left root """
    return 2*i + 1

def right(i):
    """ Calculate right root """
    return 2*i + 2

# maintain max/min heap

def exchange(A, i, j):
    """ exchange A[i] with A[j] """
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def max_heapify(A, i):
    """ Make the ith element and its roots satisfy maxheap requirements. """

    # calculate left & right root
    l = left(i)
    r = right(i)

    # compare with left root
    if l < A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    # compare with right root
    if r < A.heap_size and A[r] > A[largest]:
        largest = r

    # if exchanged with root, call recursively at root so that roots satisfy maxheap requirements.
    if largest != i:
        exchange(A, i, largest)
        max_heapify(A, largest)

def min_heapify(A, i):
    """ Make the ith element and its roots satisfy minheap requirements. """

    # calculate left & right root
    l = left(i)
    r = right(i)

    # compare with left root
    if l < A.heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i

    # compare with right root
    if r < A.heap_size and A[r] < A[smallest]:
        smallest = r

    # if exchanged with root, call recursively at root so that roots satisfy minheap requirements.
    if smallest != i:
        exchange(A, i, smallest)
        min_heapify(A, smallest)

# The functions above have time complexity O(h) where h is the height of heap.
# The functions below build max/min heap from a given unordered heap.

def build_max_heap(A):
    """ Build A into a maxheap, time complexity is O(n) """

    # initialize heap size
    A.heap_size = len(A)

    # starting from the second lowest level, call max_heapify at each element
    for i in range(A.heap_size//2 - 1, -1, -1):
        max_heapify(A, i)

def build_min_heap(A):
    """ Build min heap """
    A.heap_size = len(A)
    for i in range(A.heap_size//2 - 1, -1, -1):
        min_heapify(A, i)


# Heapsort algorithm

def heapsort(A):
    """ Time complexity is O(n*lg(n)), modify array in-place """

    # build max heap
    build_max_heap(A);

    # start from the bottom of the heap, iterate through the heap
    for i in range(len(A)-1, 0, -1):
        # exchange heap top with heap bottom
        exchange(A, 0, i)

        # pop bottom (the largest element in heap)
        A.heap_size -= 1

        # build max heap again
        max_heapify(A, 0)

# testing
A = Heap([5, 13, 2, 25, 7, 17, 20, 8, 4])
print("Before heapsort: ", A)

"""
    >>> print(A)
        [5, 13, 2, 25, 7, 17, 20, 8, 4]
    >>> A.heap_size
        9
"""

heapsort(A)
print("After heapsort: ", A)
