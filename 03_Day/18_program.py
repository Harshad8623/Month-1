a = int(input("Enter first Number  : "))
b = int(input("Enter second Number : "))
c, d = a, b
while b != 0:
    a, b = b, a % b
print(f"LCM of two numbers is : {c*d // a}")