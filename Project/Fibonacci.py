# fib(n) returns the n-th Fibonacci number
"""Fibonacci sequence is a series of numbers where every number is the
sum of the two numbers before it. The first two numbers are 0 and 1:"""


def fib(n):
    if n <= 0:
        return -1
    f = set()
    for i in range(0, n+1):
        f.add(i)

    f = list(f)

    f[0] = 0
    f[1] = 1
    list_f = [f[0], f[1]]

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
        list_f.append(f[i])

    res = (f[n-1], list_f)    # Function returns 2 values via tuple
    return res


num = int(input("Fibonacci n= "))
print("Fibonacci %s-th number= " % num, fib(num)[0])   # the appropriate value from tuple returned by function is used
print("Fibonacci list = ", fib(num)[1])                # the appropriate value from tuple returned by function is used
