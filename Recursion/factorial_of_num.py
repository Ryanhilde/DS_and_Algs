# fact(n) = fact(n-1) * n

def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n

num = input('Enter a Number: ')
n = int(num)
print(fact(n))
