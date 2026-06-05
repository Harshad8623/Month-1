age = int(input("Enter Your Age : "))
if age >= 18:
    print("You are Eligible to Vote")
    if age >= 60:
        print("You are Senior Citizen")
else:
    print("You are Not Eligible to Vote")
