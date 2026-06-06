num = int(input("Enter a Number : "))
if num <= 0:
    print("Please enter a positive number greater than zero.")
else:
    for i in range(1, num + 1):
        for j in range(num, i - 1, -1):
            print(j, end=" ")
        print()