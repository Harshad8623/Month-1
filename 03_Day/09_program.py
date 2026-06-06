num = int(input("Enter a Number : "))
if num == 0 or num == 1:
    print(F"Factorial of {num} is 1")
elif num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    print(f"The factorial of the entered number is : {factorial}")