unit = int(input("Enter Units Consumed : "))
if unit <= 100:
    bill = unit * 1.5
elif unit > 100 and unit <= 200:
    bill = 100 * 1.5 + (unit - 100) * 2.5
elif unit > 200 and unit <= 300:
    bill = 100 * 1.5 + 100 * 2.5 + (unit - 200) * 4
else:
    bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (unit - 300) * 6
print(f"Your Electricity Bill is : {bill:.2f}")
