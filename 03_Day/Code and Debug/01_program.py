total = 0
while True:
    num = int(input("Enter a Number : "))
    if num == 0:
        break
    if num > 0:
        total += num
    if num < 0:
        continue
print(f"The total of positive numbers is : {total}")