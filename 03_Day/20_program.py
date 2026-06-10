balance = 1000
pin = 9923
entered_pin = int(input("Enter ATM PIN: "))
if entered_pin == pin:
    while True:
        print("""
========== ATM MENU ==========
0. Exit
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Change PIN
==============================
""")
        choice = int(input("Enter Your Choice: "))
        if choice == 0:
            print("Thank you for using our ATM.")
            break
        elif choice == 1:
            print(f"Your Account Balance is: ₹{balance}")
        elif choice == 2:
            wd = int(input("Enter Amount to Withdraw: ₹"))
            if wd <= 0:
                print("Please enter a valid amount.")
            elif wd > balance:
                print("Insufficient Balance.")
            else:
                balance -= wd
                print(f"₹{wd} successfully withdrawn.")
                print(f"Available Balance: ₹{balance}")
        elif choice == 3:
            deposit = int(input("Enter Amount to Deposit: ₹"))
            if deposit > 0:
                balance += deposit
                print(f"₹{deposit} deposited successfully.")
                print(f"Updated Balance: ₹{balance}")
            else:
                print("Please enter a valid amount.")
        elif choice == 4:
            old_pin = int(input("Enter Old PIN: "))
            if old_pin == pin:
                new_pin = input("Enter New 4-Digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = int(new_pin)
                    print("PIN changed successfully.")
                else:
                    print("PIN must be exactly 4 digits.")
            else:
                print("Incorrect Old PIN.")
        else:
            print("Invalid Choice. Please try again.")
else:
    print("Incorrect PIN.")