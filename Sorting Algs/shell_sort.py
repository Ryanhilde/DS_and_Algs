# has O(n log n) time complexity

def shell_sort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        i = gap
        while i < n:
            temp = A[i]
            j = i - gap
            while j >= 0 and A[j] > temp:
                A[j + gap] = A[j]
                j = j - gap
            A[j + gap] = temp
            i = i + 1
        gap = gap // 2


A = [3, 5, 8, 9, 6, 2]
print("Original Array: ", A)
shell_sort(A)
print("Sorted Array: ", A)