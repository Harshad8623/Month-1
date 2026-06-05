# product of two numbers without using multiplication operator *
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
product = 0
for i in range(abs(b)):
    product += a
if b < 0:
    product = -product
print(product)