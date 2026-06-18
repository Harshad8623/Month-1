num = int(input("Enter a Number : "))
check = lambda num : "Even" if num % 2 == 0 else "Odd"
print("Square is",check(num))