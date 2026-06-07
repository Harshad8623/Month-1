num = int(input("Enter a number : "))
n = num
l = len(str(num))
total = 0
while num > 0:
    k = num % 10
    total += k ** l
    num //= 10
if total == n:
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} is not Armstrong Number")