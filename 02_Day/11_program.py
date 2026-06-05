a = int(input("Enter first side length of triangle : "))
b = int(input("Enter second side length of triangle : "))
c = int(input("Enter third side length of triangle : ")) 
if a + b > c and a + c > b and b + c > a:
    print("The given sides can form a triangle.")
else:
    print("The given sides cannot form a triangle.")