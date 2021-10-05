# The merge sort process sorts an array of length n in time complexity O(n*lg(n)).

def merge(A, p, q, r):
	# Assume A[p:q] and A[q:r] are in ascending order, this function
	# sorts A[p:r] in ascending order in time complexity of O(n).
	n1 = q - p
	n2 = r - q

	# initialize arrays, leave one space for sentinel
	L = [0 for _ in range(n1+1)]
	R = [0 for _ in range(n2+1)]
	for i in range(n1):
		L[i] = A[p+i]
	for j in range(n2):
		R[j] = A[q+j]
	L[n1] = 99999999 # sentinel
	R[n2] = 99999999
	i, j = 0, 0

	# Take two cards respectively from two piles, choose the smaller card
	for k in range(p, r):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

def merge_sort(A, p, r):
	"""
		Use the function merge(A, p, q, r) above to recursively sort an array A[p:r].
		Divide A[p:r] in half at point q, then divide again...until A[p0:q0] or A[q0:r0] has
		only 1 element. Then the merge process sorts A[p0:r0] which is then merged with its
		corresponding part. Finally the whole array A[p:r] is sorted.
	"""
	# if r <= p + 1, then the array has only 1 element, return
	if p >= r - 1:
		return
	q = int((p+r) / 2) # take floor

	# recursively merge left & right arrays
	merge_sort(A, p, q)
	merge_sort(A, q, r)
	merge(A, p, q, r)

test = [1, 5, 88, 3, 67, 35, 99, 65, 9]
print("Merge sort process begins.\nOriginal: ", test)
merge_sort(test, 0, 9)
print("After merge sort: ", test)
