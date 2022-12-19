def recursive_binary_search(A, key, l, r):
    if l > r:
        return -1
    else:
        m = (l + r) // 2
        if key == A[m]:
            return m
        elif key < A[m]:
            return recursive_binary_search(A, key, l, m - 1)
        elif key > A[m]:
            return recursive_binary_search(A, key, m + 1, r)


array = [12, 22, 34, 181, 232]
print(recursive_binary_search(array, 22, 0, len(array)-1))
