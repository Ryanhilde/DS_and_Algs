def calculate_itr(n):
    while n > 0:
        k = n ** 2
        print(k)
        n = n - 1


def calculate_rec(n):
    if n > 2:
        k = n ** 2
        print(k)
        calculate_rec(n-1)


# passes squares of 4 numbers...
calculate_itr(4)

# passes squares of 4 numbers...
calculate_rec(4)
