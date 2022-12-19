def linear_search(A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index += 1
    return -1


array = [12, 34, 22, 181, 2]
print(linear_search(array, 22))
