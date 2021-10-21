# bucket sort: works for sorting uniformly distributed numbers within [0, 1).
# expected time complexity = O(n).

def bucket_sort(A):
    """
        @brief:  sort a list of uniformly distributed numbers in [0, 1) in ascending order.
        @params: A: a list of uniformly distributed numbers in [0, 1)
        @retval: sorted array
    """
    n = len(A)

    # store n lists in B, each list is a bucket to store elements in A.
    # all buckets are expected to contain a similar number of elements.
    B = [[] for _ in range(n)]

    # insert element to buckets
    for i in range(n):
        # calculate index = floor(n*A[i])
        index = int(n*A[i])

        # insert A[i] to B[index]
        B[index].append(A[i])
    
    # sort each bucket using insertion sort (just use built-in sort here)
    for i in range(n):
        B[i].sort()
    
    # link all buckets in B in ascending order
    C = []
    for i in range(n):
        C.extend(B[i])
    
    return C

# Example:

A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
# After calling bucket_sort, B will be:
#   B = [
#           []                  <- bucket 0
#           [0.12, 0.17]        <- bucket 1
#           [0.21, 0.23, 0.26]  <- bucket 2
#           [0.39]              <- bucket 3
#           []                  <- bucket 4
#           []                  <- bucket 5
#           [0.68]              <- bucket 6
#           [0.72, 0.78]        <- bucket 7
#           []                  <- bucket 8
#           [0.94]              <- bucket 9
#       ]
if __name__ == "__main__":
    print("before sort: ", A)
    C = bucket_sort(A)
    if (C == sorted(A)):
        print("bucket_sort succeeded.")
        print("after sort: ", C)
