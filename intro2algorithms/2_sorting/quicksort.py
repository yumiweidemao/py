# Quick sort is similar to merge sort. It uses divide-and-conquer algorithm.
# Features: modify in-place, time complexity O(n*lg(n)) with a small constant coefficient.
# By contrast, merge sort requires extra memory space and time complexity O(n*lg(n)) with
# a large constant coefficient.

def exchange(A, i, j) -> None:
    """
        @brief   exchange A[i] and A[j] in-place.
        @params  A: array of numbers
                 i, j: indices
        @retval  None
    """
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# First, a function 'partition' is needed to operate on an array A and return a value
# q such that A[p:q] are all smaller than A[q], A[q+1:r+1] are all larger than A[q].
# This function will have linear time complexity = r - p + 1 = O(n).

def partition(A, p, r) -> int:
    """
        @brief   modify an array in-place such that it is divided, A[p:q] are
                 all smaller than A[q], and A[q+1:r+1] are all larger than A[q]
        @params  A: array of numbers
                 p: starting index
                 r: ending index
        @retval  q: an index such that A[q] is larger than A[p:q], smaller than A[q+1:r+1]
    """
    x = A[r]        # reference element, not randomized
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            exchange(A, i, j)
    exchange(A, i+1, r)
    return i+1

# Quick sort recursively calls 'partition' to sort an array in ascending order. 

# Divide: divide an array A[p:r] into two halves A[p:q] and A[q+1:r], where q is
#         the return value of 'partition'.
# Base case: when len(A) == 1, it is sorted. when len(A) == 2, 'partition' will sort A.
# Conquer: recursively call itself until it is true that every element in A is 'partitioned'.

def quick_sort(A, p, r) -> None:
    """
        @brief   sort an array in ascending order. Time complexity is O(n*lg(n)).
        @params  A: array of numbers
                 p: starting index
                 r: ending index
        @retval  None
    """
    # only execute if array has more than 1 element
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def test() -> None:
    """
        @brief   test function.
        @params  None
        @retval  None
    """
    # test 'partition'
    test_partition = [2, 8, 7, 1, 3, 5, 6, 4]
    print("testing partition: ")
    print("Before partition:", test_partition, " pivot index =", len(test_partition)-1)
    q = partition(test_partition, 0, len(test_partition)-1)
    print("After partition: ", test_partition, " pivot index =", q)

    # test 'quick_sort'
    test_quicksort = [8, 10, 43, 123, 635, 92, 1, 99, 32, 10]
    print("\ntesting quick_sort: ")
    quick_sort(test_quicksort, 0, len(test_quicksort)-1)
    if (test_quicksort == sorted(test_quicksort)):
        print("quick_sort succeeded.")

if __name__ == "__main__":
    test()
