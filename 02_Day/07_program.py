a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
operation = input("Enter Operation (+, -, *, /) : ")
if operation == "+":
    result = a + b
    print(f"Result of {a} + {b} is {result}")
elif operation == "-":
    result = a - b
    print(f"Result of {a} - {b} is {result}")   
elif operation == "*":
    result = a * b
    print(f"Result of {a} * {b} is {result}")
elif operation == "/":
    if b != 0:
        result = a / b
        print(f"Result of {a} / {b} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid Operation")