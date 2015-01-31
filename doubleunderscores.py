a = [1, 2, 3]

def fib(n):
    if n == 1:
        return n
    else:
        return fib(n) + fib(n-1)

print fib(3)



