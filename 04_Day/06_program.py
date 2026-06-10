for i in range(1, 10):
    if i == 1:
        print("*")
    elif i == 2:
        print("**")
    elif i == 9:
        print("*" * 9)
    else:
        print("*" + " " * (i - 2) + "*")