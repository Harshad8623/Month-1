a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
while b != 0:
    a, b = b, a % b
print("GCD =", a)