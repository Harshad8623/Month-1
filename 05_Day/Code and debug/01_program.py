def fun(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
n = int(input("Enter a Number to check even or odd : "))
print("Number is",fun(n))