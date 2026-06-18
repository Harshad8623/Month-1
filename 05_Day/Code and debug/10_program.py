n = int(input("Enter a Number : ")) # if n = 3
cube = lambda n : n ** 3
print(cube(n)) # then 27
print(cube) # <function <lambda> at 0x00000140F02BE170>
print(lambda n : n ** 3) # <function <lambda> at 0x00000140F02BE320>