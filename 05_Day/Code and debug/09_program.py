def absolute_value(n):
    if n >= 0:
        return n
    return -n
n = int(input("Enter a Number : "))
print(f"Absolute Value of {n} is {absolute_value(n)}")