n = int(input("Enter a Number : "))
check = lambda n : ("Zero" if n == 0 else "Positive") if n >= 0 else "Negative"
print(check(n))