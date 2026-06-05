num = int(input("enter a Number : "))
if num <= 0 or num >= 8:
    print(f"{num} is not between 1 and 7")
else:
    if num == 1:
        print("Monday") 
    elif num == 2:
        print("Tuesday")
    elif num == 3:  
        print("Wednesday")  
    elif num == 4:
        print("Thursday")
    elif num == 5:
        print("Friday")
    elif num == 6:
        print("Saturday")
    else:
        print("Sunday")