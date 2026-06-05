amount = int(input("Enter the amount : "))
if amount >= 5000:
    discount = amount * 0.20
    final_amount = amount - discount
    print(f"Final amount after 10% discount is : {final_amount}")
elif amount >= 2000:
    discount = amount * 0.10
    final_amount = amount - discount
    print(f"Final amount after 10% discount is : {final_amount}")
elif amount >= 1000:
    discount = amount * 0.05
    final_amount = amount - discount
    print(f"Final amount after 5% discount is : {final_amount}")
else:
    print(f"No discount applied. Final amount is : {amount}")