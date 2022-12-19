# recursive way to calculate sum of n natural numbers runs in O(n)
# note n*  (n+1) / 2 is faster

def sum_rec(n):
    if n == 0:
        return n
    return sum_rec(n-1) + n


num = input('Enter a Number: ')
n = int(num)
print(sum_rec(n))
