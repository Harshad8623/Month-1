alpha = input("Enter single Character : ")
for i in range(ord("A"), ord(alpha)+1):
    for j in range(ord("A"), i+1):
        print(chr(j), end='')
    print()