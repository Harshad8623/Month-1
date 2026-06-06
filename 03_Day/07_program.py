rev = 0
num = int(input("Enter a Number : "))
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(f"The reverse of the entered number is : {rev}")