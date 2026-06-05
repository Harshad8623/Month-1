# Check if a number is positive using and/or
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number == 0:
    print("Zero is neither positive nor negative.")
else:   
    print(f"{number} is not a positive number.")
