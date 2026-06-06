star_num = int(input("Enter the number of rows : "))
if star_num <= 0:
    print("Please enter a positive number greater than zero.")
else:
    for i in range(1, star_num + 1):
        print("*" * i)