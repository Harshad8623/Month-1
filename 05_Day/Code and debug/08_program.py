def min_of_three(a, b, c):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    return min
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))
print("Minimum is",min_of_three(a,b,c))