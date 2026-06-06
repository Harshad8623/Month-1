number = int(input("Enter a Number : "))
count = 0
while number > 0:
    number //= 10
    count += 1
print(f"The number of digits in the entered number is: {count}")