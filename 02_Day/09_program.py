num = int(input("enter a Number : "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is Divisible by both 3 and 5")
elif num % 3 == 0:
    print(f"{num} is Divisible by 3")   
elif num % 5 == 0:
    print(f"{num} is Divisible by 5")
else:
    print(f"{num} is not Divisible by either 3 or 5")