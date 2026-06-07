num = int(input("Enter a number : "))
if num <= 1:
    print(f"{num} is not prime")
elif num == 2:
    print("2 is even prime number")
else:
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            print(f"{num} is not prime number")
            break
    else:
        print(f"{num} is prime number")