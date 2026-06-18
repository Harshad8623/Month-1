def tax_calculator(income):
    if income <= 250000:
        print("No Tax")
        return 0
    elif income <= 500000:
        print("Tax : 5%")
        return income * 0.05
    elif income <= 1000000:
        print("Tax : 20%")
        return income * 0.20
    else:
        print("Tax : 30%")
        return income * 0.30
income = int(input("Enter Your Income : "))
print("Your tax amount is", tax_calculator(income))