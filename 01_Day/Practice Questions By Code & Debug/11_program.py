age = int(input("Enter Your Age : "))
is_valid_id = input("Do you have a valid ID? (yes/no) : ").lower()
if age >= 18 and is_valid_id == "yes":
    print("You can enter the club.")
else:
    print("You cannot enter the club.")