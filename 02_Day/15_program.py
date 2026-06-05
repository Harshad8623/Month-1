pin = int(input("Enter your PIN : "))
balance = 1000
if pin == 1234:
    print("PIN is correct. Access granted.")
    print("Press 1 for Balance Inquiry \nPress 2 for Cash Withdrawal \nPress 3 for Deposit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print(f"Your current balance is : {balance} rs.")
    elif choice == 2:
        amount = int(input("Enter amount to withdraw : "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful. Your new balance is : {balance} rs.")
    elif choice == 3:
        amount = int(input("Enter amount to deposit : "))
        balance += amount
        print(f"Deposit successful. Your new balance is : {balance} rs.")
else:
    print("Incorrect PIN. Access denied.")