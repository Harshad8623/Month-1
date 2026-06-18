def discount_price(original_price, discount_percent):
    return original_price * (100 - discount_percent)/100
o = int(input("Enter Original price : "))
d = int(input("Enter Discount Percentage : "))
print("Your Final Price After Discount is", discount_price(o, d))