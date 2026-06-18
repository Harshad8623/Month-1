def factorial(num):
    fact = 1
    a = num
    if num < 0:
        print("Factorial is Undefined")
        return None
    if num == 0 or num == 1:
        return 1
    while a > 0:
        fact *= a
        a -= 1
    return fact
print(factorial(4))