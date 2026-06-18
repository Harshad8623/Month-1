def fun(*args):
    total = 0
    for i in args:
        total += i
    return total
print(fun(1, 2, 3, 4, 5, 6))
print(fun(1, 2, 3))
print(fun(7, 8))
print(fun(1, 2, 3, 4, 5))