sub1 = int(input("Enter Marks of Subject 1 : "))
sub2 = int(input("Enter Marks of Subject 2 : "))
sub3 = int(input("Enter Marks of Subject 3 : "))
total = sub1 + sub2 + sub3
print(f"Total Marks : {total}")
percentage = (total / 300) * 100
print(f"Percentage : {percentage}%")
average = total / 3
print(f"Average Marks : {average}")