# counting sort: does not use any comparison operation. Can be within linear time complexity.

# Theorem: any sorting algorithm that uses comparison has minimum time complexity O(n*lg(n)).
# (can be proven by the decision tree model)

# For an array A of n elements in a range of width k, counting sort has time complexity O(n+k), 
# which can be reduced to O(n) if k is not much larger than n.

def counting_sort(A):
    """
        @brief  sort an array in ascending order.
        @params A: array of numbers
        @retval B: array of sorted numbers in A
    """
    n = len(A)
    assert (min(A) >= 0)
    k = max(A)

    # initialize two arrays B and C
    B = [0 for _ in range(n)]       # B is the output array
    C = [0 for _ in range(k+1)]       # C[i] is the number of occurence of i in A

    # for num in A, count occurence and record in C[num]
    for i in range(n):
        C[A[i]] = C[A[i]] + 1
    
    # C[i] now contains the number of elements equal to i.
    # Now make C[i] contain the number of elements less than or equal to i.
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    
    # put each element in the right place by referring to C
    for i in range(n):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1            # in case of duplicate elements
    
    return B

def test():
    test_A = [7, 8, 10, 22, 45, 1, 0, 22, 2, 2, 1, 7, 8]
    if (sorted(test_A) == counting_sort(test_A)):
        print("counting_sort succeeded.")
        print("before sorted: ", test_A)
        print("after sorted: ", counting_sort(test_A))

if __name__ == "__main__":
    test()
