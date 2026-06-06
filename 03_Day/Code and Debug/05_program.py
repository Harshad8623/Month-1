num = int(input("Enter a Number : "))
if num <= 0:
    print("Please enter a positive number greater than zero.")
else:
    for i in range(num, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()