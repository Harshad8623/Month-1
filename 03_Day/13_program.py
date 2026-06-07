total = 0
num = int(input("Enter a number : "))
while num != 0:        # num > 0 also ok
    digit = num % 10
    total += digit
    num //= 10
print("Sum of all digits is :",total)