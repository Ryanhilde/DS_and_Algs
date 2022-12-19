# O(N) in best case, O(n^2) in worst case
# Works well if you already have a mostly sorted array

def bubble_sort(A):
    n = len(A)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp


A = [3, 5, 8, 9, 6, 2]
print("Original Array: ", A)
bubble_sort(A)
print("Sorted Array: ", A)
