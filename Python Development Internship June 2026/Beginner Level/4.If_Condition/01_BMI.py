# This program calculates the Body Mass Index (BMI) based on user input for height and weight, and categorizes the BMI into different health categories.
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
BMI = weight/height**2
print(f"BMI: {BMI:.2f}")
if BMI >= 30:
    print("Obesity")

elif BMI >= 25:
    print("Overweight")

elif BMI >= 18.5:
    print("Normal")

else:
    print("Underweight")