weight = int(input("Enter your weight in kg : "))
height = int(input("Enter your height in cm : "))
bmi = weight / ((height / 100) ** 2)
print(f"Your BMI is : {bmi:.2f}")
if bmi < 18.5:
    print("You are Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are Normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")
    