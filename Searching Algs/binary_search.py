def binary_search(A, key):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if key == A[m]:
            return m
        elif key < A[m]:
            r = m - 1
        elif key > A[m]:
            l = m + 1
    return -1


array = [12, 22, 34, 181, 232]
print(binary_search(array, 22))
