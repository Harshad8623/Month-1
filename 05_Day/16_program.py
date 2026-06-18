def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
terms = 10
fibonacci(terms)


# or

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)

# or Using a List

n = 10
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(fib)

# Print Nth Fibonacci Number

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(fib(10))
