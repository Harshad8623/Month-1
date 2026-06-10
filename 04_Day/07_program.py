for i in range(10, 0, -1):
    if i in (10, 2, 1):
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")