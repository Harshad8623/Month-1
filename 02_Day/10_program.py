import datetime
print("Press \n1. Enter your age \n2. Enter your DOB")
choice = int(input("Enter your choice : "))
if choice == 1: 
    age = int(input("Enter your Age : "))
else:
    dob = input("Enter your Date of Birth (DD/MM/YYYY) : ")
    day, month, year = map(int, dob.split('/'))
    age = datetime.date.today().year - year
print(f"Your Age is : {age} years")

if age < 12:
    print("Ticket price is 15 rs.")
elif age < 60:
    print("Ticket price is 100 rs.")
else:
    print("Ticket price is 50 rs.")