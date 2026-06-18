def find_max1(a, b, c):
    if a >= b:
        if a >= c:
            return a
        return c
    else:
        if b >= c:
            return b
        return c

while True:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    c = int(input("Enter Third Number : "))
    print("Maximum is", find_max1(a, b, c))


# or

while True:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    c = int(input("Enter Third Number : "))

    print("Maximum is", max(a, b, c))

# or

def find_max2(a, b, c):
    maximum = a

    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c

    return maximum
print("Maximum is", find_max2(a, b, c))