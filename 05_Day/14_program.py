num = 10
a = 12
def fun():
    num = 20
    global a
    a = 18
    print("Inside num value",num)
    print("Inside a value",a)

fun()
print("Outside num value",num)
print("Outside a value",a)