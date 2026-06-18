def fun(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count

s = input("Enter String : ").lower()
print(fun(s))