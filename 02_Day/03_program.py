a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))
if a > b and a > c:
    print(f"{a} is the greatest number.")
elif b > a and b > c:
    print(f"{b} is the greatest number.")
else:
    print(f"{c} is the greatest number.")