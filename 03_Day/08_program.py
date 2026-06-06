rev = 0
num = int(input("Enter a Number : "))
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if rev == num:
    print(f"The entered number is a palindrome.")
else:
    print(f"The entered number is not a palindrome.")