is_citizen = input("Are you a citizen of the country? (yes/no): ").lower()
age = int(input("Enter your age: "))
if is_citizen == "yes" and age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")