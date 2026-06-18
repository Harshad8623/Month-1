def power(base, exp):
    e = exp
    result = 1
    while e > 0:
        result *= base
        e -= 1
    return result
base = int(input("Enter Base Value : "))
exp = int(input("Enter Exp Value : "))
print(power(base, exp))